"use strict";
//インポート
import { sql_limit } from "./conf.js";
//コンポーネント
const TODO_HEADER_TOP = {
    path: "/TODO_HEADER_TOP/:PAGE",
    component: {
        template: "#TODO_HEADER_TOP",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                values: null,
                title: "作業一覧",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function() {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_HEADER_TOP/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            PAGE_BUTTON: function(tg) {
                this.$router.push(`/TODO_HEADER_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
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
const TODO_HEADER_FORM = {
    path: "/TODO_HEADER_FORM",
    component: {
        template: "#TODO_HEADER_FORM",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                TODO_HEADER_ID: null,
                TODO_HEADER_NAME: null,
                GENRE_NAME: null,
                PRIOR_NAME: null,
                TODO_HEADER_DATE:null,
                values_GENRE: [
                    []
                ],
                values_PRIOR: [
                    []
                ],
                button_name: "登録",
                title: "作業フォーム",
            }
        },
        methods: {
            axios_GET: function() {
                axios.get("http://192.168.10.100:8080/COM/NOW_TIME/")
                    .then(res => {
                        this.TODO_HEADER_DATE = res.data.values;
                    });
                axios.get("http://192.168.10.100:8080/TODO/TODO_HEADER_FORM/")
                    .then(res => {
                        this.values_GENRE = res.data.values_GENRE;
                    });
            },
            axios_POST: function() {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("TODO_HEADER_DATE", this.TODO_HEADER_DATE);
                console.log(params);
                axios.post(`http://192.168.10.100:8080/TODO/TODO_HEADER_FORM/`, params)
                    .then(res => {})
            },
        },
        created: function() {
            this.axios_GET();
        }
    }
};
const TODO_HEADER_FORM_UPDATE = {
    path: "/TODO_HEADER_FORM/:TODO_HEADER_ID",
    component: {
        template: "#TODO_HEADER_FORM",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                TODO_HEADER_ID: null,
                TODO_HEADER_NAME: null,
                GENRE_NAME: null,
                TODO_HEADER_DATE: null,
                values_GENRE: [
                    []
                ],
                button_name: "更新",
                title: "作業フォーム",
            }
        },
        methods: {
            axios_GET: function() {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_HEADER_FORM/${this.$route.params.TODO_HEADER_ID}`)
                    .then(res => {
                        this.TODO_HEADER_ID = res.data.values[0][0];
                        this.TODO_HEADER_NAME = res.data.values[0][1];
                        this.GENRE_NAME = res.data.values[0][2];
                        this.TODO_HEADER_DATE = res.data.values[0][3];
                        this.values_GENRE = res.data.values_GENRE;
                        console.log(res);
                    })
            },
            axios_POST: function() {
                const params = new URLSearchParams();
                params.append("TODO_HEADER_ID", this.TODO_HEADER_ID);
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("TODO_HEADER_DATE", this.TODO_HEADER_DATE);
                axios.post(`http://192.168.10.100:8080/TODO/TODO_HEADER_FORM/${this.$route.params.TODO_HEADER_ID}`, params)
                    .then(res => {})
            },
        },
        created: function() {
            this.axios_GET();
        }
    }
}
const TODO_HEADER_TOP_DEL = {
    path: "/TODO_HEADER_TOP_DEL/:PAGE",
    component: {
        template: "#TODO_HEADER_TOP",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                values: null,
                title: "作業一覧_削除",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function() {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_HEADER_TOP_DEL/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            PAGE_BUTTON: function(tg) {
                this.$router.push(`/TODO_HEADER_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function() {
                this.nav_menu = !this.nav_menu;
            }
        },
        created: function() {
            this.axios_GET();
        }
    }
};

export { TODO_HEADER_TOP, TODO_HEADER_FORM, TODO_HEADER_FORM_UPDATE, TODO_HEADER_TOP_DEL, }