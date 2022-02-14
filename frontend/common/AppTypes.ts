import React from "react";

export interface AccountResponse {
    id: string;
    uuid: string;
    email: string;
    username: string;
    is_active: boolean;
    created: Date;
    updated: Date;
    access: string;
    refresh: string;
}

export type State = {
    access_token: string | null;
    refresh_token: string | null;
    account: AccountResponse | null;
};

export interface AuthTokensType {
    access: string | null;
    refresh: string | null;
}

export interface AccountDetailsType {
    email: string,
    password: string
}

type SuccessCallback = (res?: any) => void;
type ErrorCallback = (err: any) => void;

export interface FunctionCallbackType {
    success?: SuccessCallback,
    failure?: ErrorCallback,
    completed?: VoidFunction,
}

export interface AuthContextState {
    user: AccountResponse,
    tokens: AuthTokensType
}

export interface AuthContextType {
    user: AccountResponse;
    tokens: AuthTokensType;
    dispatch: React.Dispatch<any>;
    register?: ({username, email, password}, {success, failure, completed}: FunctionCallbackType) => void;
    signin?: ({email, password}: AccountDetailsType, {success, failure, completed}: FunctionCallbackType) => void;
    signout?: ({success, failure, completed}?: FunctionCallbackType) => void;
}
