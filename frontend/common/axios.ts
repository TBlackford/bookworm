import axios from 'axios';
import createAuthRefreshInterceptor from 'axios-auth-refresh';

import store from '@common/store';
import { logout, setAuthTokens } from "@/features/authentication/auth";
import { postRefresh } from "@/common/BaseApi";

const axiosService = axios.create({
    baseURL: process.env.REACT_APP_API_URL,
    headers: {
        //'Content-Type': 'application/json',
    },
});

axiosService.interceptors.request.use(async (config: any) => {
    const {access_token} = store.getState().auth;

    if (access_token !== null) {
        config.headers.Authorization = 'Bearer ' + access_token;
        // @ts-ignore
        console.debug('[Request]', config.baseURL + config.url, JSON.stringify(access_token));
    }
    return config;
});

axiosService.interceptors.response.use(
    (res) => {
        // @ts-ignore
        console.debug('[Response]', res.config.baseURL + res.config.url, res.status, res.data);
        return Promise.resolve(res);
    },
    (err) => {
        console.debug(
            '[Response]',
            err.config.baseURL + err.config.url,
            err.response.status,
            err.response.data
        );
        return Promise.reject(err);
    }
);

// @ts-ignore
const refreshAuthLogic = async (failedRequest) => {
    const {refresh_token} = store.getState().auth;
    if (refresh_token !== null) {
        return postRefresh({refresh: refresh_token}, {
            success: res => {
                const {access, refresh} = res.data;
                failedRequest.response.config.headers.Authorization = 'Bearer ' + access;
                store.dispatch(
                    setAuthTokens({token: access, refreshToken: refresh})
                );
            },
            failure: err => {
                if (err.response && err.response.status === 401) {
                    store.dispatch(logout());
                }
            }
        })
    }
};

//TODO: fix this constantly refreshing when the user want to log out
createAuthRefreshInterceptor(axiosService, refreshAuthLogic);

export function fetcher<T = any>(url: string) {
    return axiosService.get<T>(url).then((res) => res.data);
}

export default axiosService;
