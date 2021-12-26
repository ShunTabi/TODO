"use strict";
//インポート
import { sql_limit, url } from "./conf.js";
const l_sql_limit = sql_limit - 3;
//コンポーネント
const MEMO_TOP = {
    path: "/MEMO_TOP/:PAGE",
    component: {
        template: "#MEMO_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "メモ一覧",
                page_max: null,
                nav_menu: false,
                TODO_HEADER_ID: 0,
                values_TODO_HEADER: [[]],
                GOAL_ID: 0,
                values_GOAL: [[]],
                value_MEMO_CONTENT: "",
            }
        },
        methods: {
            axios_GET: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("value_MEMO_CONTENT", this.value_MEMO_CONTENT);
                axios.get(`${url}TODO/MEMO_TOP/${this.$route.params.PAGE}`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / l_sql_limit);
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_GOAL = res.data.values_GOAL;
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/MEMO_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/MEMO_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function () {
                this.nav_menu = !this.nav_menu;
            },
        },
        created: function () {
            this.axios_GET();
            this.nav_menu = false;
        }
    }
};
const MEMO_TOP_DEL = {
    path: "/MEMO_TOP_DEL/:PAGE",
    component: {
        template: "#MEMO_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "メモ一覧_削除",
                page_max: null,
                nav_menu: false,
                TODO_DETAIL_ID: 0,
                values_TODO_DETAIL: [[]],
                value_MEMO_CONTENT: "",
            }
        },
        methods: {
            axios_GET: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("value_MEMO_CONTENT", this.value_MEMO_CONTENT);
                axios.get(`${url}TODO/MEMO_TOP_DEL/${this.$route.params.PAGE}`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / l_sql_limit);
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/MEMO_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/MEMO_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function () {
                this.nav_menu = !this.nav_menu;
            },
        },
        created: function () {
            this.axios_GET();
            this.nav_menu = false;
        }
    }
};
const MEMO_FORM = {
    path: "/MEMO_FORM",
    component: {
        template: "#MEMO_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                MEMO_ID: null,
                TODO_HEADER_ID: 0,
                values_TODO_HEADER: [[]],
                TODO_DETAIL_ID: 0,
                values_TODO_DETAIL: [[]],
                MEMO_CONTENT: null,
                MEMO_DATE: null,
                VISIBLESTATUS: 0,
                button_name: "登録",
                title: "メモフォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}COM/NOW_TIME/`)
                    .then(res => {
                        this.MEMO_DATE = res.data.values;
                    });
                axios.get(`${url}TODO/MEMO_FORM/`)
                    .then(res => {
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_DETAIL_ID", this.TODO_DETAIL_ID);
                params.append("MEMO_CONTENT", this.MEMO_CONTENT);
                params.append("MEMO_DATE", this.MEMO_DATE);
                params.append("MEMO_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/MEMO_FORM/`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
const MEMO_FORM_UPDATE = {
    path: "/MEMO_FORM/:MEMO_ID",
    component: {
        template: "#MEMO_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                MEMO_ID: null,
                TODO_HEADER_ID: 0,
                values_TODO_HEADER: [[]],
                TODO_DETAIL_ID: 0,
                values_TODO_DETAIL: [[]],
                MEMO_CONTENT: null,
                MEMO_DATE: null,
                VISIBLESTATUS: 0,
                button_name: "更新",
                title: "メモフォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`)
                    .then(res => {
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;
                        this.MEMO_ID = res.data.values[0][0];
                        this.TODO_HEADER_ID = res.data.values[0][1];
                        this.TODO_DETAIL_ID = res.data.values[0][2];
                        this.MEMO_CONTENT = res.data.values[0][3];
                        this.MEMO_DATE = res.data.values[0][4];
                        this.VISIBLESTATUS = res.data.values[0][5];
                    })
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("MEMO_ID", this.MEMO_ID);
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_DETAIL_ID", this.TODO_DETAIL_ID);
                params.append("MEMO_CONTENT", this.MEMO_CONTENT);
                params.append("MEMO_DATE", this.MEMO_DATE);
                params.append("MEMO_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};

export { MEMO_TOP, MEMO_FORM, MEMO_FORM_UPDATE, MEMO_TOP_DEL }