from django.apps import AppConfig
from django.core.management.base import AppCommand

from ts_generator.utils import (
    export_serializer,
    get_app_routers,
    get_module_serializers,
    get_nested_serializers,
    get_project_routers,
    get_serializer_fields, )


class Command(AppCommand):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project_routers = get_project_routers()
        self.already_parsed_serializers = set()
        self.already_parsed_api_endpoints = set()

    def add_arguments(self, parser):
        parser.add_argument(
            '--format', type=str, choices=['type', 'interface'], default='type',
            help='Specifies whether the result will be types or interfaces'
        )
        parser.add_argument(
            '--preserve-case', action='store_true', default=False,
            help='Preserve field name case from serializers'
        )
        parser.add_argument(
            '--semicolons', action='store_true', default=False,
            help='Semicolons will be added if this argument is present'
        )
        whitespace_group = parser.add_mutually_exclusive_group()
        whitespace_group.add_argument('--spaces', type=int, default=2)
        whitespace_group.add_argument('--tabs', type=int)

        return super().add_arguments(parser)

    def handle_app_config(self, app_config: AppConfig, **options):

        # find routers in app urls and project urls
        routers = [router[1] for router in self.project_routers + get_app_routers(app_config.name)]
        views_modules = set()
        api_endpoints = dict()
        serializers = set()

        # find modules containing viewsets in the app (views.py, api.py, etc.)
        for router in routers:
            for _prefix, viewset_class, _basename in router.registry:
                module = viewset_class.__module__
                views_modules.add(module)

                request_data = None

                if hasattr(viewset_class, 'Meta'):
                    if hasattr(viewset_class.Meta, 'request_data'):
                        request_data = viewset_class.Meta.request_data

                # Get the endpoint data
                api_endpoints.update({
                    module: {
                        'path': viewset_class.path,
                        'name': viewset_class.name or module.split('.')[-1].replace('ViewSet', ''),
                        'method': viewset_class.method,
                        'request_data': request_data
                    }
                })

        # extract all serializers found in views modules
        for module in views_modules:
            serializers = serializers.union(get_module_serializers(module))

            if len(get_module_serializers(module)) > 0:
                serializer_set = get_module_serializers(module)
                old_data = api_endpoints.get(module)

                endpoint = {
                    'return': serializer_set[0][0]
                }

                api_endpoints.update({
                    module: endpoint | old_data
                })

        self.process_file(serializers, api_endpoints, options)

    def process_file(self, serializers, api_endpoints, options):

        # Write some important stuff first
        self.stdout.write("""// We have a custom axios client
import axios from "@common/axios";
import { AxiosResponse } from "axios";

export type SuccessCallback = (res?: any) => void;
export type ErrorCallback = (err: any) => void;

export type ApiPromise<T> = Promise<void | AxiosResponse<any, any> | T>;

export interface FunctionCallbackType {
    success?: SuccessCallback,
    failure?: ErrorCallback,
    completed?: VoidFunction,
}

const api = (url: string, data?: {}, functionCallbackType?: FunctionCallbackType) => {
    return axios
        .post(url + '/', data)
        .then((res) => {
            if(functionCallbackType && functionCallbackType.success) {
                functionCallbackType.success(res);
            }
            return res;
        })
        .catch((res) => {
            if(functionCallbackType && functionCallbackType.failure) {
                functionCallbackType.failure(res);
            }
        })
        .finally(() => {
            if(functionCallbackType && functionCallbackType.completed) {
                functionCallbackType.completed();
            }
        });
}\n\n""")

        # Types will end up here later

        for serializer_name, serializer in sorted(serializers):
            self.process_serializer(serializer_name, serializer, options)

        for (key, value) in api_endpoints.items():
            self.process_api_endpoint(key, value)

    def process_api_endpoint(self, endpoint, endpoint_data):
        for method in endpoint_data['method']:
            endpoint_name = method + endpoint_data['name']
            request_data = endpoint_data['request_data']
            data_str = None

            if request_data is None:
                first_line = f"export const {endpoint_name} = (functionCallbackType?: FunctionCallbackType)"
            else:
                first_line = f"export const {endpoint_name} = ("
                data_str = f"{{"

                for i, data in enumerate(request_data):
                    if i == len(request_data) - 1:
                        data_str += f"{data}}}"
                    else:
                        data_str += f"{data}, "

                first_line += f"{data_str}, functionCallbackType?: FunctionCallbackType)"

            first_line += f" => {{"
            # if 'return' in endpoint_data:
            #     first_line += f": ApiPromise<{endpoint_data['return']}> => {{"
            # else:
            #     first_line += f" => {{"

            self.stdout.write(first_line)
            if request_data is None and data_str is None:
                self.stdout.write(f"\treturn api('{endpoint_data['path']}', functionCallbackType);")
            else:
                self.stdout.write(f"\treturn api('{endpoint_data['path']}', {data_str}, functionCallbackType);")
            self.stdout.write("}\n\n")

    def process_serializer(self, serializer_name, serializer, options):
        if serializer_name not in self.already_parsed_serializers:
            # recursively process nested serializers first to ensure that
            # TS equivalent is generated even if they are not used in views module
            nested_serializers = get_nested_serializers(serializer)
            for nested_serializer_name, nested_serializer in nested_serializers.items():
                self.process_serializer(nested_serializer_name, nested_serializer, options)

            fields = get_serializer_fields(serializer, options)
            ts_serializer = export_serializer(serializer_name, fields, options)
            self.already_parsed_serializers.add(serializer_name)
            self.stdout.write(ts_serializer)
