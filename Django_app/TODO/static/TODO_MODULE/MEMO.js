"use strict";
//インポート
import { axios_GET, axios_POST, ZeroPadding, isShowTrue, checkPage, } from './COM.js';
import { Lancher_header, Lancher_detail, isShow, button_names, par_null, len_search_key, mes_placeholder, } from './conf.js';
//コンポーネント
const MEMO_ = {
    path: "/MEMO_/:par/:page/:key_MEMO",
    name: "MEMO_",
    component: {
        template: "#MEMO_",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                //TOP ELEMENTS
                Code: 3,
                Lancher_header: [],
                Lancher_detail: [],
                values: [[]],
                page: null,
                max_page: null,
                //FORM ELEMENTS
                values_GOAL: [[]],
                values_TODO_HEADER: [[]],
                values_TODO_DETAIL: [[]],
                //FORM ELEMENTS
                GOAL_ID: null,
                TODO_HEADER_ID: null,
                TODO_DETAIL_ID: null,
                MEMO_CONTENT: null,
                //SETTINGS
                isShow: isShow,
                button_name: null,
                button_names: button_names,
                MEMO_FORM: isShow,
                MEMO_TOP: isShow,
                MEMO_SEARCH: isShow,
                //UPDATE PARAMETERS
                TODO_DETAIL_ID: null,
                //SEARCH PARAMETERS
                key_MEMO: null,
                len_search_key: len_search_key,
                mes_placeholder: mes_placeholder,
                par_null: par_null,
            }
        },
        methods: {
            l_axios_GET: function () {
                if (this.key_MEMO == "") {
                    this.key_MEMO = par_null;
                };
                axios_GET(`TODO/MEMO_TOP/${this.$route.params.page}/${this.key_MEMO}`, "", (res) => {
                    this.values = res.data.values;
                    this.max_page = checkPage(Math.ceil(res.data.count / res.data.sql_limit));
                });
            },
            l_axios_GET_FORM: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                axios_GET("TODO/MEMO_FORM/", params, (res) => {
                    if (this.GOAL_ID == null) {
                        this.values_GOAL = res.data.values_GOAL;
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;

                    } else {
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;
                    }
                });
            },
            l_axios_GET_UPDATE: function (MEMO_ID) {
                const params = new URLSearchParams();
                params.append("MEMO_ID", MEMO_ID);
                axios_GET("TODO/MEMO_UPDATE/", params, (res) => {
                    this.MEMO_ID = res.data.values[0][0];
                    this.TODO_DETAIL_ID = res.data.values[0][1];
                    this.MEMO_CONTENT = res.data.values[0][2];
                    this.button_name = button_names[1];
                });
            },
            change_key_MEMO: function () {
                this.$router.push(`/MEMO_/${this.$route.params.par}/1/${this.key_MEMO}`);
            },
            next_page: function () {
                this.$router.push(`/MEMO_/${this.$route.params.par}/${(Number(this.page) + 1)}/${this.$route.params.key_MEMO}`);
            },
            pre_page: function () {
                this.$router.push(`/MEMO_/${this.$route.params.par}/${Number(this.page) - 1}/${this.$route.params.key_MEMO}`);
            },
            clearForm: function () {
                this.MEMO_ID = null;
                this.TODO_DETAIL_ID = null;
                this.MEMO_CONTENT = null;
                this.button_name = button_names[0];
            },
            l_axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_DETAIL_ID", this.TODO_DETAIL_ID);
                params.append("MEMO_CONTENT", this.MEMO_CONTENT);
                if (this.TODO_MEMO_ID != null) {
                    params.append("MEMO_ID", this.MEMO_ID);
                    axios_POST("TODO/MEMO_UPDATE/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                } else {
                    axios_POST("TODO/MEMO_FORM/", params, () => {
                        this.l_axios_GET();
                        this.clearForm();
                    });
                }
            },
            l_axios_POST_DEL: function (MEMO_ID) {
                const params = new URLSearchParams();
                params.append("MEMO_ID", MEMO_ID);
                axios_POST("TODO/MEMO_DEL/", params, () => {
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
                this.button_name = this.button_names[0]
                this.key_MEMO = this.$route.params.key_MEMO
                this.l_axios_GET();
                this.l_axios_GET_FORM();
                this.l_isShowTrue(this.$route.params.par, (params) => {
                    this.MEMO_TOP = params[0];
                    this.MEMO_FORM = params[1];
                    this.MEMO_SEARCH = params[2];
                });
                if (this.key_MEMO == par_null) {
                    this.key_MEMO = "";
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
export { MEMO_ }