"use strict";
//インポート
import { sql_limit } from "./conf.js";
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
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_DETAIL_TOP/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`http://192.168.10.100:8080/TODO/TODO_DETAIL_DEL/${tg}`)
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
            }
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
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_DETAIL_TOP_DEL/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`http://192.168.10.100:8080/TODO/TODO_DETAIL_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/TODO_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function () {
                this.nav_menu = !this.nav_menu;
            }
        },
        created: function () {
            this.axios_GET();
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
                TODO_DETAIL_NAME: null,
                PRIOR_NAME: null,
                TODO_HEADER_NAME: null,
                TODO_DETAIL_STARTDATE: null,
                TODO_DETAIL_ENDDATE: null,
                values_PRIOR: [
                    []
                ],
                values_TODO_HEADER: [
                    []
                ],
                button_name: "登録",
                title: "課題フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get("http://192.168.10.100:8080/COM/NOW_TIME/")
                    .then(res => {
                        this.TODO_DETAIL_STARTDATE = res.data.values;
                        this.TODO_DETAIL_ENDDATE = res.data.values;
                    });
                axios.get("http://192.168.10.100:8080/TODO/TODO_DETAIL_FORM/")
                    .then(res => {
                        this.values_PRIOR = res.data.values_PRIOR;
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("TODO_DETAIL_NAME", this.TODO_DETAIL_NAME);
                params.append("PRIOR_NAME", this.PRIOR_NAME);
                params.append("TODO_DETAIL_STARTDATE", this.TODO_DETAIL_STARTDATE);
                params.append("TODO_DETAIL_ENDDATE", this.TODO_DETAIL_ENDDATE);
                console.log(params);
                axios.post(`http://192.168.10.100:8080/TODO/TODO_DETAIL_FORM/`, params)
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
                TODO_DETAIL_NAME: null,
                PRIOR_NAME: null,
                TODO_HEADER_NAME: null,
                TODO_DETAIL_STARTDATE: null,
                TODO_DETAIL_ENDDATE: null,
                values_PRIOR: [
                    []
                ],
                values_TODO_HEADER: [
                    []
                ],
                button_name: "更新",
                title: "課題フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_DETAIL_FORM/${this.$route.params.TODO_DETAIL_ID}`)
                    .then(res => {
                        this.TODO_DETAIL_ID = res.data.values[0][0];
                        this.TODO_HEADER_NAME = res.data.values[0][1];
                        this.TODO_DETAIL_NAME = res.data.values[0][2];
                        this.PRIOR_NAME = res.data.values[0][3];
                        this.TODO_DETAIL_STARTDATE = res.data.values[0][4];
                        this.TODO_DETAIL_ENDDATE = res.data.values[0][5];
                        this.values_PRIOR = res.data.values_PRIOR;
                        this.values_TODO_HEADER = res.data.values_TODO_HEADER;
                    })
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("TODO_DETAIL_NAME", this.TODO_DETAIL_NAME);
                params.append("PRIOR_NAME", this.PRIOR_NAME);
                params.append("TODO_DETAIL_STARTDATE", this.TODO_DETAIL_STARTDATE);
                params.append("TODO_DETAIL_ENDDATE", this.TODO_DETAIL_ENDDATE);
                axios.post(`http://192.168.10.100:8080/TODO/TODO_DETAIL_FORM/${this.$route.params.TODO_DETAIL_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
}

export { TODO_DETAIL_TOP, TODO_DETAIL_FORM, TODO_DETAIL_FORM_UPDATE, TODO_DETAIL_TOP_DEL, }