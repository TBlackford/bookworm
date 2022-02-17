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

export type AuthorSerializer = {
    createdTimestamp?: string
    firstName: string
    fullName: string
    lastName: string
    modifiedTimestamp?: string
    uuid?: string
}

export type UserSerializer = {
    createdTimestamp: string
    email?: string | null
    isActive?: boolean
    modifiedTimestamp: string
    username: string
    uuid?: string
}

export type LoginSerializer = {
    access?: string
    refresh?: string
    user?: UserSerializer
}

export type RegisterSerializer = {
    email: string
    isActive?: boolean
    password: string
    username: string
    uuid?: string
}

export const postLogin = ({email, password}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/login', 'post', {email, password}, functionCallbackType);
}

export const postLogout = ({refresh}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/logout', 'post', {refresh}, functionCallbackType);
}

export const postRegistration = ({username, email, password}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/register', 'post', {username, email, password}, functionCallbackType);
}

export const postRefresh = ({refresh}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/refresh', 'post', {refresh}, functionCallbackType);
}

export const getUser = (functionCallbackType?: FunctionCallbackType) => {
	return api('user', 'get', functionCallbackType);
}

export const getAuthor = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'get', functionCallbackType);
}

export const postAuthor = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'post', functionCallbackType);
}

export const deleteAuthor = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'delete', functionCallbackType);
}

export const putAuthor = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'put', functionCallbackType);
}

