"use strict";
const openWindow_1 = function (url, windowName) {
    alert("Hello");
    console.log("Hello");
    info = 'toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,left=0,top=0,resizable=yes,width=1014,height=740,title=no';
    const window1 = window.open(url, windowName, info);
    window1.moveTo(0, 0);
    window.opener = self;
    window.close();
}
const start_url = 'http://192.168.10.100:8080/TODO/#/TODO_HEADER_TOP/1'
const start_WindowName = '_blank'
const start_option = 'menubar=0,toolbar=0,location=0,status=0,resizable=0'

const openWindow = function (url, WindowName, option) {
    window.open(url, WindowName, option);
}
export { openWindow, start_url, start_WindowName, start_option }
