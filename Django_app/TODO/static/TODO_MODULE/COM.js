"use strict";
import { default_url, sec, len_charactor, len_integer, } from "./conf.js";

//GET通信
const axios_GET = (url, params, callback) => {
    console.log(`${default_url}${url}`);
    if (params == "") {
        axios.get(`${default_url}${url}`)
            .then(res => {
                setTimeout(() => {
                    callback(res)
                }, sec)
            })
    } else {
        axios.get(`${default_url}${url}`, { "params": params })
            .then(res => {
                setTimeout(() => {
                    callback(res)
                }, sec)
            })
    }
};

//POST通信
const axios_POST = (url, params, callback) => {
    axios.post(`${default_url}${url}`, params)
        .then(res => {
            setTimeout(() => {
                callback(res)
            }, sec)
        })
};

//メッセージ出力
const sendMessage = (Message, hint, code) => {
    window.alert(Message);
};

//スタートアップ
const AppStartup = (start_url) => {
    const start_WindowName = '_blank'
    const start_option = "menubar=0,toolbar=0,location=0,status=0,resizable=0,left=0,top=0,width=1100,height=600"
    const openWindow = (url, WindowName, option) => {
        window.open(url, WindowName, option);
        window.opener = self;
        window.close();
    }
    openWindow(start_url, start_WindowName, start_option);
};

const ZeroPadding = (tg) => {
    return (Array(len_integer).join('0') + tg).slice(-len_integer);
};

const isShowTrue = (par, callback) => {
    const params = [];
    if (par == "0") {
        params.push(true, false, true);
    } else if (par == "1") {
        params.push(false, true, false);
    } else if (par == "2") {
        params.push(true, true, false);
    }
    callback(params);
};

const checkPage = (max_page) => {
    if (max_page == 0) {
        max_page = 1
    }
    return max_page;
}

export { axios_GET, axios_POST, sendMessage, AppStartup, ZeroPadding, isShowTrue, checkPage, }