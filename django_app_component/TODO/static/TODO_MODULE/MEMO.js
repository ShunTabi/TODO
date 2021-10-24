"use strict";
//インポート
<<<<<<< HEAD
import { sql_limit } from "./conf.js";
=======
import { sql_limit,url } from "./conf.js";
>>>>>>> DEV
//コンポーネント
const MEMO_TOP = {
    path: "/MEMO_TOP/:PAGE",
    component: {
        template: "#MEMO_TOP",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                values: null,
                title: "メモ一覧",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function() {
<<<<<<< HEAD
                axios.get(`http://192.168.10.100:8080/TODO/MEMO_TOP/${this.$route.params.PAGE}`)
=======
                axios.get(`${url}TODO/MEMO_TOP/${this.$route.params.PAGE}`)
>>>>>>> DEV
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
<<<<<<< HEAD
=======
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/MEMO_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
>>>>>>> DEV
            PAGE_BUTTON: function(tg) {
                this.$router.push(`/MEMO_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function() {
                this.nav_menu = !this.nav_menu;
            }
        },
        created: function() {
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
        data: function() {
            return {
                MEMO_ID: null,
<<<<<<< HEAD
                TODO_NAME: null,
                MEMO_NOTE: null,
                MEMO_DATE: null,
                values_TODO: [
=======
                TODO_DETAIL_NAME: null,
                MEMO_NOTE: null,
                MEMO_DATE: null,
                VISIBLESTATUS: 0,
                values_TODO_DETAIL: [
>>>>>>> DEV
                    []
                ],
                button_name: "登録",
                title: "メモフォーム",
            }
        },
        methods: {
            axios_GET: function() {
<<<<<<< HEAD
                axios.get("http://192.168.10.100:8080/COM/NOW_TIME/")
                    .then(res => {
                        this.MEMO_DATE = res.data.values;
                    });
                axios.get("http://192.168.10.100:8080/TODO/MEMO_FORM/")
                    .then(res => {
                        this.values_TODO = res.data.values_TODO;
                    });
            },
            axios_POST: function() {
                const params = new URLSearchParams();
                params.append("TODO_NAME", this.TODO_NAME);
                params.append("MEMO_NOTE", this.MEMO_NOTE);
                params.append("MEMO_DATE", this.MEMO_DATE);
                axios.post("http://192.168.10.100:8080/TODO/MEMO_FORM/", params)
                    .then(res => {})
=======
                axios.get(`${url}COM/NOW_TIME/`)
                    .then(res => {
                        this.MEMO_DATE = res.data.values;
                    });
                axios.get(`${url}TODO/MEMO_FORM/`)
                    .then(res => {
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_DETAIL_NAME", this.TODO_DETAIL_NAME);
                params.append("MEMO_NOTE", this.MEMO_NOTE);
                params.append("MEMO_DATE", this.MEMO_DATE);
                params.append("MEMO_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/MEMO_FORM/`, params)
                    .then(res => { })
>>>>>>> DEV
            },
        },
        created: function() {
            this.axios_GET();
        }
    }
};
const MEMO_FORM_UPDATE = {
    path: "/MEMO_FORM/:MEMO_ID",
    component: {
        template: "#MEMO_FORM",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
<<<<<<< HEAD
                MEMO_ID: null,
                TODO_NAME: null,
                MEMO_NOTE: null,
                MEMO_DATE: null,
                values_TODO: [
=======
                TODO_DETAIL_NAME: null,
                MEMO_NOTE: null,
                MEMO_DATE: null,
                VISIBLESTATUS: 0,
                values_TODO_DETAIL: [
>>>>>>> DEV
                    []
                ],
                button_name: "更新",
                title: "メモフォーム",
            }
        },
        methods: {
            axios_GET: function() {
<<<<<<< HEAD
                axios.get(`http://192.168.10.100:8080/TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`)
                    .then(res => {
                        this.MEMO_ID = res.data.values[0][0];
                        this.TODO_NAME = res.data.values[0][1];
                        this.MEMO_NOTE = res.data.values[0][2];
                        this.MEMO_DATE = res.data.values[0][3];
                        this.values_TODO = res.data.values_TODO;
=======
                axios.get(`${url}TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`)
                    .then(res => {
                        this.MEMO_ID = res.data.values[0][0];
                        this.TODO_DETAIL_NAME = res.data.values[0][1];
                        this.MEMO_NOTE = res.data.values[0][2];
                        this.MEMO_DATE = res.data.values[0][3];
                        this.VISIBLESTATUS = res.data.values[0][4];
                        this.values_TODO_DETAIL = res.data.values_TODO_DETAIL;
>>>>>>> DEV
                    })
            },
            axios_POST: function() {
                const params = new URLSearchParams();
                params.append("MEMO_ID", this.MEMO_ID);
<<<<<<< HEAD
                params.append("TODO_NAME", this.TODO_NAME);
                params.append("MEMO_NOTE", this.MEMO_NOTE);
                params.append("MEMO_DATE", this.MEMO_DATE);
                axios.post(`http://192.168.10.100:8080/TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`, params)
=======
                params.append("TODO_DETAIL_NAME", this.TODO_DETAIL_NAME);
                params.append("MEMO_NOTE", this.MEMO_NOTE);
                params.append("MEMO_DATE", this.MEMO_DATE);
                params.append("MEMO_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`, params)
>>>>>>> DEV
                    .then(res => {})
            },
        },
        created: function() {
            this.axios_GET();
        }
    }
}
const MEMO_TOP_DEL = {
    path: "/MEMO_TOP_DEL/:PAGE",
    component: {
        template: "#MEMO_TOP",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                values: null,
                title: "メモ一覧_削除",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function() {
<<<<<<< HEAD
                axios.get(`http://192.168.10.100:8080/TODO/MEMO_TOP_DEL/${this.$route.params.PAGE}`)
=======
                axios.get(`${url}TODO/MEMO_TOP_DEL/${this.$route.params.PAGE}`)
>>>>>>> DEV
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
<<<<<<< HEAD
=======
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/MEMO_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
>>>>>>> DEV
            PAGE_BUTTON: function(tg) {
                this.$router.push(`/MEMO_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function() {
                this.nav_menu = !this.nav_menu;
            }
        },
        created: function() {
            this.axios_GET();
            this.nav_menu = false;
        }
    }
};

export { MEMO_TOP, MEMO_FORM, MEMO_FORM_UPDATE, MEMO_TOP_DEL }