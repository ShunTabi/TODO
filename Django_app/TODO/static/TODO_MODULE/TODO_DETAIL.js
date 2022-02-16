"use strict";
//インポート
import { axios_GET, axios_POST, ZeroPadding, isShowTrue, checkPage, } from './COM.js';
import { Lancher_header, Lancher_detail, isShow, button_names, par_null, len_search_key, mes_placeholder, } from './conf.js';
//コンポーネント
const TODO_DETAIL_ = {
    path: "/TODO_DETAIL_/:par/:page/:key_TODO/:key_STATUS_ID",
    name: "TODO_DETAIL_",
    component: {
        template: "#TODO_DETAIL_",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                //TOP ELEMENTS
                Code: 2,
                Lancher_header: [],
                Lancher_detail: [],
                values: [[]],
                page: null,
                max_page: null,
                //FORM ELEMENTS
                values_GOAL: [[]],
                values_TODO_HEADER: [[]],
                values_STATUS: [[]],
                //SEND PARAMETERS
                GOAL_ID: null,
                TODO_HEADER_ID: null,
                STATUS_ID: null,
                TODO_DETAIL_NAME: null,
                TODO_DETAIL_STARTDATE: null,
                TODO_DETAIL_ENDDATE: null,
                //SETTINGS
                isShow: isShow,
                button_name: null,
                button_names: button_names,
                TODO_DETAIL_FORM: isShow,
                TODO_DETAIL_TOP: isShow,
                TODO_DETAIL_SEARCH: isShow,
                //UPDATE PARAMETERS
                TODO_DETAIL_ID: null,
                //SEARCH PARAMETERS
                key_TODO: null,
                key_STATUS_ID: null,
                keyValeus_STATUS: [[]],
                len_search_key: len_search_key,
                mes_placeholder: mes_placeholder,
                par_null: par_null,
            }
        },
        methods: {
            l_axios_GET: function () {
                if (this.key_TODO == "") {
                    this.key_TODO = par_null;
                };
                axios_GET(`TODO/TODO_DETAIL_TOP/${this.$route.params.page}/${this.key_TODO}/${this.key_STATUS_ID}`, "", (res) => {
                    this.values = res.data.values;
                    this.max_page = checkPage(Math.ceil(res.data.count / res.data.sql_limit));
                    this.keyValeus_STATUS = res.data.values_STATUS;
                });
            },
            l_axios_GET_FORM: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                axios_GET("TODO/TODO_DETAIL_FORM/", params, (res) => {
                    if (this.GOAL_ID == null) {
                        this.values_GOAL = res.data.values_GOAL;
                        this.values_STATUS = res.data.values_STATUS;
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.TODO_DETAIL_STARTDATE = res.data.values_nowtime;
                        this.TODO_DETAIL_ENDDATE = res.data.values_nowtime;
                    } else {
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                    }
                });
            },
            l_axios_GET_UPDATE: function (TODO_DETAIL_ID) {
                const params = new URLSearchParams();
                params.append("TODO_DETAIL_ID", TODO_DETAIL_ID);
                axios_GET("TODO/TODO_DETAIL_UPDATE/", params, (res) => {
                    this.TODO_DETAIL_ID = res.data.values[0][0];
                    this.TODO_HEADER_ID = res.data.values[0][1];
                    this.STATUS_ID = res.data.values[0][2];
                    this.TODO_DETAIL_NAME = res.data.values[0][3];
                    this.TODO_DETAIL_STARTDATE = res.data.values[0][4];
                    this.TODO_DETAIL_ENDDATE = res.data.values[0][5];
                    this.button_name = button_names[1];
                });
            },
            change_key_TODO: function () {
                if (this.key_TODO == "") {
                    this.key_TODO = par_null;
                };
                this.$router.push(`/TODO_DETAIL_/${this.$route.params.par}/1/${this.key_TODO}/${this.$route.params.key_STATUS_ID}`);
            },
            change_key_STATUS_ID: function () {
                this.$router.push(`/TODO_DETAIL_/${this.$route.params.par}/1/${this.$route.params.key_TODO}/${this.key_STATUS_ID}`);
            },
            next_page: function () {
                this.$router.push(`/TODO_DETAIL_/${this.$route.params.par}/${(Number(this.page) + 1)}/${this.$route.params.key_TODO}/${this.$route.params.key_STATUS_ID}`);
            },
            pre_page: function () {
                this.$router.push(`/TODO_DETAIL_/${this.$route.params.par}/${Number(this.page) - 1}/${this.$route.params.key_TODO}/${this.$route.params.key_STATUS_ID}`);
            },
            clearForm: function () {
                this.GOAL_ID = null;
                this.TODO_HEADER_ID = null;
                this.TODO_DETAIL_ID = null;
                this.STATUS_ID = null;
                this.TODO_DETAIL_NAME = null;
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                axios_GET("TODO/TODO_DETAIL_FORM/", params, (res) => {
                    this.TODO_DETAIL_STARTDATE = res.data.values_nowtime;
                    this.TODO_DETAIL_ENDDATE = res.data.values_nowtime;
                });
                this.button_name = button_names[0];
            },
            l_axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("STATUS_ID", this.STATUS_ID);
                params.append("TODO_DETAIL_NAME", this.TODO_DETAIL_NAME);
                params.append("TODO_DETAIL_STARTDATE", this.TODO_DETAIL_STARTDATE);
                params.append("TODO_DETAIL_ENDDATE", this.TODO_DETAIL_ENDDATE);
                if (this.TODO_DETAIL_ID != null) {
                    params.append("TODO_DETAIL_ID", this.TODO_DETAIL_ID);
                    axios_POST("TODO/TODO_DETAIL_UPDATE/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                } else {
                    axios_POST("TODO/TODO_DETAIL_FORM/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                }
            },
            l_axios_POST_DEL: function (TODO_DETAIL_ID) {
                const params = new URLSearchParams();
                params.append("TODO_DETAIL_ID", TODO_DETAIL_ID);
                axios_POST("TODO/TODO_DETAIL_DEL/", params, () => {
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
                this.key_STATUS_ID = this.$route.params.key_STATUS_ID;
                this.key_TODO = this.$route.params.key_TODO;
                this.l_axios_GET();
                this.l_axios_GET_FORM();
                this.l_isShowTrue(this.$route.params.par, (params) => {
                    this.TODO_DETAIL_TOP = params[0];
                    this.TODO_DETAIL_FORM = params[1];
                    this.TODO_DETAIL_SEARCH = params[2];
                });
                if (this.key_TODO == par_null) {
                    this.key_TODO = "";
                };
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
export { TODO_DETAIL_ }