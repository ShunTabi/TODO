"use strict";
import { router } from './TODO_MODULE/router.js';
import { Lancher_header, Lancher_detail, isShow } from './TODO_MODULE/conf.js';
//APP
const app = new Vue({
    el: "#app",
    router: router,
    delimiters: ["[[", "]]"],
    data: {
        Lancher_SECTION_MAIN_FIRST_status: isShow,
        Lancher_SECTION_MAIN_status: isShow,
        LANCHER_HEADERs: Lancher_header,
        LANCHER_DETAILs: Lancher_detail,
    },
    methods: {
        ONOFF_Lancher_SECTION_MAIN: function () {
            this.Lancher_SECTION_MAIN_status = !this.Lancher_SECTION_MAIN_status;
        },
    },
    created() {
    }
});