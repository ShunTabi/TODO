"use strict";
//インポート
import { axios_GET, axios_POST, ZeroPadding, isShowTrue, checkPage, } from './COM.js';
import { Lancher_header, Lancher_detail, isShow, button_names, } from './conf.js';
//コンポーネント
const GENRE = {
    path: "/GENRE/:par/:page",
    name: "GENRE",
    component: {
        template: "#GENRE",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                //TOP ELEMENTS
                Code: 4,
                Lancher_header: [],
                Lancher_detail: [],
                values: [[]],
                page: null,
                max_page: null,
                //SEND PARAMETERS
                GENRE_NAME: null,
                //SETTINGS
                isShow: isShow,
                button_name: null,
                button_names: button_names,
                GENRE_FORM: isShow,
                GENRE_TOP: isShow,
                //UPDATE_PARAMETERS
                GENRE_ID: null,
            }
        },
        methods: {
            l_axios_GET: function () {
                axios_GET(`TODO/GENRE_TOP/${this.$route.params.page}`, "", (res) => {
                    this.values = res.data.values;
                    this.max_page = checkPage(Math.ceil(res.data.count / res.data.sql_limit));
                });
            },
            l_axios_GET_UPDATE: function (GENRE_ID) {
                const params = new URLSearchParams();
                params.append("GENRE_ID", GENRE_ID);
                axios_GET("TODO/GENRE_UPDATE/", params, (res) => {
                    this.GENRE_ID = res.data.values[0][0];
                    this.GENRE_NAME = res.data.values[0][1];
                    this.button_name = button_names[1];
                });
            },
            next_page: function () {
                this.$router.push(`/GENRE/${this.$route.params.par}/${(Number(this.page) + 1)}`);
            },
            pre_page: function () {
                this.$router.push(`/GENRE/${this.$route.params.par}/${Number(this.page) - 1}`);
            },
            clearForm: function () {
                this.GENRE_NAME = null;
                this.GENRE_ID = null;
                this.button_name = button_names[0];
            },
            l_axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GENRE_NAME", this.GENRE_NAME);
                if (this.GENRE_ID != null) {
                    params.append("GENRE_ID", this.GENRE_ID);
                    axios_POST("TODO/GENRE_UPDATE/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                } else {
                    axios_POST("TODO/GENRE_FORM/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                }
            },
            l_axios_POST_DEL: function (GENRE_ID) {
                const params = new URLSearchParams();
                params.append("GENRE_ID", GENRE_ID);
                axios_POST("TODO/GENRE_DEL/", params, () => {
                    this.l_axios_GET();
                    this.clearForm();
                });
            },
            l_ZeroPadding: function (tg) {
                return ZeroPadding(tg);
            },
            l_isShowTrue: function (par, callback) {
                isShowTrue(par, callback);
            },
            l_startup: function () {
                this.Lancher_header = Lancher_header[this.Code];
                this.Lancher_detail = Lancher_detail[this.Code];
                this.button_name = button_names[0];
                this.page = this.$route.params.page;
                this.l_axios_GET();
                this.l_isShowTrue(this.$route.params.par, (params) => {
                    this.GENRE_TOP = params[0];
                    this.GENRE_FORM = params[1];
                });
            },
        },
        created: function () {
            this.l_startup();
        },
        beforeRouteUpdate(to, from, next) {
            next();
            this.l_startup();
        },
    }
};
export { GENRE }