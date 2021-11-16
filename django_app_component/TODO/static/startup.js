"use strict";
import { start_url } from "./TODO_MODULE/conf.js";
const start_WindowName = '_blank'
const start_option = "menubar=no,toolbar=no,location=0,status=0,resizable=0,left=0,top=0,width=1100,height=600"
const openWindow = function (url, WindowName, option) {
    window.open(url, WindowName, option);
    window.opener = self;
    window.close();
}
openWindow(start_url, start_WindowName, start_option);