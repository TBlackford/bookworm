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

export type AppUserSerializer = {
    createdTimestamp?: string
    email?: string | null
    isActive?: boolean
    modifiedTimestamp?: string
    username?: string
    uuid?: string
}

export type AuthorSerializer = {
    archivedTimestamp?: string
    createdTimestamp?: string
    deletedTimestamp?: string
    firstName?: string
    fullName?: string
    lastName?: string
    modifiedTimestamp?: string
    uuid?: string
}

export type BookSerializer = {
    archivedTimestamp?: string
    author?: AuthorSerializer
    createdTimestamp?: string
    deletedTimestamp?: string
    firstPubDate?: string
    format?: string
    isbn?: string
    language?: string
    modifiedTimestamp?: string
    pages?: number
    pubDate?: string
    rating?: number
    title?: string
    uuid?: string
}

export type LoginSerializer = {
    access?: string
    refresh?: string
    user?: AppUserSerializer
}

export type RegisterSerializer = {
    email?: string
    isActive?: boolean
    password?: string
    username?: string
    uuid?: string
}

export const postLoginInterface = ({email, password}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/login', 'post', {email, password}, functionCallbackType);
}

export const postLogoutInterface = ({refresh}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/logout', 'post', {refresh}, functionCallbackType);
}

export const postRegistrationInterface = ({username, email, password}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/register', 'post', {username, email, password}, functionCallbackType);
}

export const postRefreshInterface = ({refresh}, functionCallbackType?: FunctionCallbackType) => {
	return api('auth/refresh', 'post', {refresh}, functionCallbackType);
}

export const getUserInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('user', 'get', functionCallbackType);
}

export const getAuthorInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'get', functionCallbackType);
}

export const postAuthorInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'post', functionCallbackType);
}

export const deleteAuthorInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'delete', functionCallbackType);
}

export const putAuthorInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('author', 'put', functionCallbackType);
}

export const getBookInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('book', 'get', functionCallbackType);
}

export const postBookInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('book', 'post', functionCallbackType);
}

export const deleteBookInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('book', 'delete', functionCallbackType);
}

export const putBookInterface = (functionCallbackType?: FunctionCallbackType) => {
	return api('book', 'put', functionCallbackType);
}

