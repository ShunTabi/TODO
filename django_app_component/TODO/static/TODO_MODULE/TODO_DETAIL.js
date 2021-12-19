"use strict";
//インポート
import { sql_limit, url } from "./conf.js";
const l_sql_limit = sql_limit;
//コンポーネント
const TODO_DETAIL_TOP = {
    path: "/TODO_DETAIL_TOP/:PAGE",
    component: {
        template: "#TODO_DETAIL_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "課題一覧",
                page_max: null,
                nav_menu: false,
                TODO_HEADER_ID: 0,
                values_TODO_HEADER: [[]],
                value_TODO_DETAIL_CONTENT: "",
            }
        },
        methods: {
            axios_GET: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_DETAIL_CONTENT", this.value_TODO_DETAIL_CONTENT);
                axios.get(`${url}TODO/TODO_DETAIL_TOP/${this.$route.params.PAGE}`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / l_sql_limit);
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/TODO_DETAIL_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/TODO_DETAIL_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function () {
                this.nav_menu = !this.nav_menu;
            },
            CHANGE_nav_TODO_HEADER_ID() {
                this.axios_GET();
            },
            CHANGE_nav_TODO_DETAIL_CONTENT() {
                this.axios_GET();
            },
        },
        created: function () {
            this.axios_GET();
            this.nav_menu = false;
        }
    }
};
const TODO_DETAIL_TOP_DEL = {
    path: "/TODO_DETAIL_TOP_DEL/:PAGE",
    component: {
        template: "#TODO_DETAIL_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "課題一覧_削除",
                page_max: null,
                nav_menu: false,
                TODO_HEADER_ID: 0,
                values_TODO_HEADER: [[]],
                value_TODO_DETAIL_CONTENT: "",
            }
        },
        methods: {
            axios_GET: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_DETAIL_CONTENT", this.value_TODO_DETAIL_CONTENT);
                axios.get(`${url}TODO/TODO_DETAIL_TOP_DEL/${this.$route.params.PAGE}`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / l_sql_limit);
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/TODO_DETAIL_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/TODO_DETAIL_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function () {
                this.nav_menu = !this.nav_menu;
            },
            CHANGE_nav_TODO_HEADER_ID() {
                this.axios_GET();
            },
            CHANGE_nav_TODO_DETAIL_CONTENT() {
                this.axios_GET();
            },
        },
        created: function () {
            this.axios_GET();
            this.nav_menu = false;
        }
    }
};
const TODO_DETAIL_FORM = {
    path: "/TODO_DETAIL_FORM",
    component: {
        template: "#TODO_DETAIL_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                TODO_DETAIL_ID: null,
                TODO_HEADER_ID: null,
                TODO_DETAIL_CONTENT: null,
                TODO_DETAIL_DATE: null,
                VISIBLESTATUS: 0,
                values_TODO_HEADER: [[]],
                STATUS_ID: 2,//デフォルト値として「未」で設定
                values_STATUS: [[]],
                button_name: "登録",
                title: "課題フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}COM/NOW_TIME/`)
                    .then(res => {
                        this.TODO_DETAIL_DATE = res.data.values;
                    });
                axios.get(`${url}TODO/TODO_DETAIL_FORM/`)
                    .then(res => {
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_STATUS = res.data.values_STATUS;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_DETAIL_CONTENT", this.TODO_DETAIL_CONTENT);
                params.append("TODO_DETAIL_DATE", this.TODO_DETAIL_DATE);
                params.append("STATUS_ID", this.STATUS_ID);
                params.append("TODO_DETAIL_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/TODO_DETAIL_FORM/`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
const TODO_DETAIL_FORM_UPDATE = {
    path: "/TODO_DETAIL_FORM/:TODO_DETAIL_ID",
    component: {
        template: "#TODO_DETAIL_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                TODO_DETAIL_ID: null,
                TODO_HEADER_ID: null,
                TODO_DETAIL_CONTENT: null,
                TODO_DETAIL_DATE: null,
                VISIBLESTATUS: 0,
                values_TODO_HEADER: [[]],
                STATUS_ID: null,//デフォルト値として「未」で設定
                values_STATUS: [[]],
                button_name: "更新",
                title: "課題フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/TODO_DETAIL_FORM/${this.$route.params.TODO_DETAIL_ID}`)
                    .then(res => {
                        this.TODO_DETAIL_ID = res.data.values[0][0];
                        this.TODO_HEADER_ID = res.data.values[0][1];
                        this.TODO_DETAIL_CONTENT = res.data.values[0][2];
                        this.TODO_DETAIL_DATE = res.data.values[0][4];
                        this.STATUS_ID = res.data.values[0][3];
                        this.VISIBLESTATUS = res.data.values[0][5];
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_STATUS = res.data.values_STATUS;
                    })
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_DETAIL_ID", this.TODO_DETAIL_ID);
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_DETAIL_CONTENT", this.TODO_DETAIL_CONTENT);
                params.append("TODO_DETAIL_DATE", this.TODO_DETAIL_DATE);
                params.append("STATUS_ID", this.STATUS_ID);
                params.append("TODO_DETAIL_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/TODO_DETAIL_FORM/${this.$route.params.TODO_DETAIL_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};

export { TODO_DETAIL_TOP, TODO_DETAIL_FORM, TODO_DETAIL_FORM_UPDATE, TODO_DETAIL_TOP_DEL }