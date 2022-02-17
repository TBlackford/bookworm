// We have a custom axios client
import axios from "@common/axios";
import { AxiosResponse, Method } from "axios";

export type SuccessCallback = (res?: any) => void;
export type ErrorCallback = (err: any) => void;

export type ApiPromise<T> = Promise<void | AxiosResponse<any, any> | T>;

export interface FunctionCallbackType {
    success?: SuccessCallback,
    failure?: ErrorCallback,
    completed?: VoidFunction,
}

const api = (url: string, method: Method, data?: {}, functionCallbackType?: FunctionCallbackType) => {
    return axios.request({
        url: url + '/',
        data
    })
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
}