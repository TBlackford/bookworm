import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import { AccountResponse, State } from "@common/AppTypes";


const initialState: State = {
    access_token: null,
    refresh_token: null,
    account: null
};

const authSlice = createSlice({
    name: "auth",
    initialState,
    reducers: {
        setAuthTokens(state: State, action: PayloadAction<{ token: string; refreshToken: string }>) {
            state.refresh_token = action.payload.refreshToken;
            state.access_token = action.payload.token;
        },
        setAccount(state: State, action: PayloadAction<AccountResponse>) {
            state.account = action.payload;
        },
        login(state: State, action: PayloadAction<{ token: string; refreshToken: string }>) {
            state.refresh_token = action.payload.refreshToken;
            state.access_token = action.payload.token;
        },
        logout(state: State) {
            state = initialState;
        },
    },
});

export const {setAuthTokens, setAccount, logout, login} = authSlice.actions;

export default authSlice.reducer
