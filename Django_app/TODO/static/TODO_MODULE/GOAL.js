"use strict";
//インポート
import { axios_GET, axios_POST, ZeroPadding, isShowTrue, } from './COM.js';
import { Lancher_header, Lancher_detail, isShow, button_names, } from './conf.js';
//コンポーネント
const GOAL_ = {
    path: "/GOAL_/:par/:page",
    name: "GOAL_",
    component: {
        template: "#GOAL_",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                //TOP ELEMENTS
                Code: 0,
                Lancher_header: [],
                Lancher_detail: [],
                values: [[]],
                page: null,
                max_page: null,
                //FORM ELEMENTS
                values_GENRE: [[]],
                //SEND PARAMETERS
                GENRE_ID: null,
                GOAL_NAME: null,
                //SETTINGS
                isShow: isShow,
                button_name: null,
                button_names: button_names,
                GOAL_FORM: isShow,
                GOAL_TOP: isShow,
                //UPDATE_PARAMETERS
                GOAL_ID: null,
            }
        },
        methods: {
            l_axios_GET: function () {
                axios_GET(`TODO/GOAL_TOP/${this.$route.params.page}`, "", (res) => {
                    this.values = res.data.values;
                    this.max_page = Math.ceil(res.data.count / res.data.sql_limit);
                });
            },
            l_axios_GET_FORM: function () {
                axios_GET("TODO/GOAL_FORM/", "", (res) => {
                    this.values_GENRE = res.data.values_GENRE;
                });
            },
            l_axios_GET_UPDATE: function (GOAL_ID) {
                const params = new URLSearchParams();
                params.append("GOAL_ID", GOAL_ID);
                axios_GET("TODO/GOAL_UPDATE/", params, (res) => {
                    this.GOAL_ID = res.data.values[0][0];
                    this.GENRE_ID = res.data.values[0][1];
                    this.GOAL_NAME = res.data.values[0][2];
                    this.button_name = button_names[1];
                });
            },
            next_page: function () {
                this.$router.push(`/GOAL_/${this.$route.params.par}/${(Number(this.page) + 1)}`);
            },
            pre_page: function () {
                this.$router.push(`/GOAL_/${this.$route.params.par}/${Number(this.page) - 1}`);
            },
            clearForm: function () {
                this.GOAL_ID = null;
                this.GENRE_ID = null;
                this.GOAL_NAME = null;
                this.button_name = button_names[0];
            },
            l_axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GENRE_ID", this.GENRE_ID);
                params.append("GOAL_NAME", this.GOAL_NAME);
                if (this.GOAL_ID != null) {
                    params.append("GOAL_ID", this.GOAL_ID);
                    axios_POST("TODO/GOAL_UPDATE/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                } else {
                    axios_POST("TODO/GOAL_FORM/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                }
            },
            l_axios_POST_DEL: function (GOAL_ID) {
                const params = new URLSearchParams();
                params.append("GOAL_ID", GOAL_ID);
                axios_POST("TODO/GOAL_DEL/", params, () => {
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
                this.page = this.$route.params.page;
                this.button_name = button_names[0];
                this.l_axios_GET();
                this.l_axios_GET_FORM();
                this.l_isShowTrue(this.$route.params.par, (params) => {
                    this.GOAL_TOP = params[0];
                    this.GOAL_FORM = params[1];
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
export { GOAL_ }