"use strict";
//インポート
import { axios_GET, axios_POST, ZeroPadding, isShowTrue, } from './COM.js';
import { Lancher_header, Lancher_detail, isShow, button_names, par_null, len_search_key, mes_placeholder, } from './conf.js';
//コンポーネント
const TODO_HEADER_ = {
    path: "/TODO_HEADER_/:par/:page/:key",
    name: "TODO_HEADER_",
    component: {
        template: "#TODO_HEADER_",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                //TOP ELEMETS
                Code: 1,
                Lancher_header: [],
                Lancher_detail: [],
                values: [[]],
                page: null,
                max_page: null,
                //FORM ELEMETS
                values_GOAL: [[]],
                values_PRIOR: [[]],
                //SEND PARAMETERS
                GOAL_ID: null,
                PRIOR_ID: null,
                TODO_HEADER_NAME: null,
                TODO_HEADER_ENDDATE: null,
                //SETTINGS
                isShow: isShow,
                button_name: null,
                button_names: button_names,
                TODO_HEADER_FORM: isShow,
                TODO_HEADER_TOP: isShow,
                TODO_HEADER_SEARCH: isShow,
                //UPDATE PARAMETERS
                TODO_HEADER_ID: null,
                //SEARCH PARAMETERS
                key_TODO_HEADER_NAME: null,
                len_search_key: len_search_key,
                mes_placeholder: mes_placeholder,
                par_null: par_null,
            }
        },
        methods: {
            l_axios_GET: function () {
                axios_GET(`TODO/TODO_HEADER_TOP/${this.$route.params.page}/${this.key_TODO_HEADER_NAME}`, "", (res) => {
                    this.values = res.data.values;
                    this.max_page = Math.ceil(res.data.count / res.data.sql_limit);
                });
            },
            l_axios_GET_FORM: function () {
                axios_GET("TODO/TODO_HEADER_FORM/", "", (res) => {
                    this.values_GOAL = res.data.values_GOAL;
                    this.values_PRIOR = res.data.values_PRIOR;
                    this.TODO_HEADER_ENDDATE = res.data.values_nowtime;
                });
            },
            l_axios_GET_UPDATE: function (TODO_HEADER_ID) {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", TODO_HEADER_ID);
                axios_GET("TODO/TODO_HEADER_UPDATE/", params, (res) => {
                    this.TODO_HEADER_ID = res.data.values[0][0];
                    this.GOAL_ID = res.data.values[0][1];
                    this.PRIOR_ID = res.data.values[0][2];
                    this.TODO_HEADER_NAME = res.data.values[0][3];
                    this.TODO_HEADER_ENDDATE = res.data.values[0][4];
                    this.button_name = button_names[1];
                });
            },
            change_key_TODO_HEADER_NAME: function () {
                if (this.key_TODO_HEADER_NAME == "") {
                    this.key_TODO_HEADER_NAME = par_null;
                };
                this.$router.push(`/TODO_HEADER_/${this.$route.params.par}/1/${this.key_TODO_HEADER_NAME}`);
            },
            next_page: function () {
                this.$router.push(`/TODO_HEADER_/${this.$route.params.par}/${(Number(this.page) + 1)}/${this.$route.params.key}`);
            },
            pre_page: function () {
                this.$router.push(`/TODO_HEADER_/${this.$route.params.par}/${Number(this.page) - 1}/${this.$route.params.key}`);
            },
            clearForm: function () {
                this.TODO_HEADER_ID = null;
                this.GOAL_ID = null;
                this.PRIOR_ID = null;
                this.TODO_HEADER_NAME = null;
                axios_GET("TODO/TODO_HEADER_FORM/", "", (res) => {
                    this.TODO_HEADER_ENDDATE = res.data.values_nowtime;
                })
                this.button_name = button_names[0];
            },

            l_axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("PRIOR_ID", this.PRIOR_ID);
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("TODO_HEADER_ENDDATE", this.TODO_HEADER_ENDDATE);
                if (this.TODO_HEADER_ID != null) {
                    params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                    axios_POST("TODO/TODO_HEADER_UPDATE/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                } else {
                    axios_POST("TODO/TODO_HEADER_FORM/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                }
            },
            l_axios_POST_DEL: function (TODO_HEADER_ID) {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", TODO_HEADER_ID);
                axios_POST("TODO/TODO_HEADER_DEL/", params, () => {
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
                this.button_name = this.button_names[0];
                this.key_TODO_HEADER_NAME = this.$route.params.key;
                this.l_axios_GET();
                this.l_axios_GET_FORM();
                this.l_isShowTrue(this.$route.params.par, (params) => {
                    this.TODO_HEADER_TOP = params[0];
                    this.TODO_HEADER_FORM = params[1];
                    this.TODO_HEADER_SEARCH = params[2];
                });
                if (this.key_TODO_HEADER_NAME == par_null) {
                    this.key_TODO_HEADER_NAME = "";
                }
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
export { TODO_HEADER_ }