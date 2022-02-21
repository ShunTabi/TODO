"use strict";
//インポート
import {
    axios_GET,
    axios_POST,
    ZeroPadding,
    isShowTrue,
    checkPage,
    check_len_DAYOFWEEK,
} from './COM.js';
import {
    Lancher_header,
    Lancher_detail,
    isShow,
    button_names,
    par_null,
    len_search_key,
    mes_placeholder,
} from './conf.js';
//コンポーネント
const TODO_MANAGE = {
    path: "/TODO_MANAGE/:par/:page/:key1/:key2/:key_TODO",
    name: "TODO_MANAGE",
    component: {
        template: "#TODO_MANAGE",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                //TOP ELEMENTS
                Code: 5,
                Lancher_header: [],
                Lancher_detail: [],
                values: [[]],
                page: null,
                max_page: null,
                len_search_key: len_search_key,
                mes_placeholder: mes_placeholder,
                //SEND PARAMETERS
                //SETTINGS
                isShow: isShow,
                //UPDATE_PARAMETERS
                //SEARCH PARAMETERS
                search_key_startdate: "",
                search_key_enddate: "",
                key_TODO: null,

            }
        },
        methods: {
            l_axios_GET: function () {
                axios_GET(`TODO/TODO_MANAGE_TOP/${this.$route.params.page}/${this.$route.params.key1}/${this.$route.params.key2}/${this.$route.params.key_TODO}`, "", (res) => {
                    this.values = res.data.values;
                    this.max_page = checkPage(Math.ceil(res.data.count / res.data.sql_limit));
                    console.log(res.data);
                });
            },
            change_key_TODO: function () {
                if (this.key_TODO == "") {
                    this.key_TODO = par_null;
                };
                this.$router.push(`/TODO_MANAGE/${this.$route.params.par}/1/${this.$route.params.key1}/${this.$route.params.key2}/${this.key_TODO}`);
            },
            change_key_date: function () {
                this.$router.push(`/TODO_MANAGE/${this.$route.params.par}/${(this.$route.params.page)}/${this.search_key_startdate}/${this.search_key_enddate}/${this.$route.params.key_TODO}`);
            },
            next_page: function () {
                this.$router.push(`/TODO_MANAGE/${this.$route.params.par}/${(Number(this.page) + 1)}/${this.$route.params.key1}/${this.$route.params.key2}/${this.$route.params.key_TODO}`);
            },
            pre_page: function () {
                this.$router.push(`/TODO_MANAGE/${this.$route.params.par}/${Number(this.page) - 1}/${this.$route.params.key1}/${this.$route.params.key2}/${this.$route.params.key_TODO}`);
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
                this.search_key_startdate = this.$route.params.key1;
                this.search_key_enddate = this.$route.params.key2;
                this.key_TODO = this.$route.params.key_TODO;
                this.button_name = button_names[0];
                this.page = this.$route.params.page;
                this.l_axios_GET();
                if (this.key_TODO == par_null) {
                    this.key_TODO = "";
                };
            },
            check_len_DAYOFWEEK: function (tg) {
                return check_len_DAYOFWEEK(tg);
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
export { TODO_MANAGE }