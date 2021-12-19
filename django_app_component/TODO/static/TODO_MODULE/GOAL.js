"use strict";
//インポート
import { sql_limit, url } from "./conf.js";
//コンポーネント
const GOAL_TOP = {
    path: "/GOAL_TOP/:PAGE",
    component: {
        template: "#GOAL_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "目標一覧",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/GOAL_TOP/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/GOAL_DEL/${tg}`)
                    .then(res => {

                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/GOAL_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
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
const GOAL_TOP_DEL = {
    path: "/GOAL_TOP_DEL/:PAGE",
    component: {
        template: "#GOAL_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "目標一覧_削除",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/GOAL_TOP_DEL/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/GOAL_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/GOAL_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
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
const GOAL_FORM = {
    path: "/GOAL_FORM",
    component: {
        template: "#GOAL_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                GOAL_ID: null,
                GOAL_NAME: null,
                GENRE_ID: null,
                GOAL_DATE: null,
                VISIBLESTATUS: 0,
                values_GENRE: [
                    []
                ],
                button_name: "登録",
                title: "目標フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}COM/NOW_TIME/`)
                    .then(res => {
                        this.GOAL_DATE = res.data.values;
                    });
                axios.get(`${url}TODO/GOAL_FORM/`)
                    .then(res => {
                        this.values_GENRE = res.data.values_GENRE;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GOAL_NAME", this.GOAL_NAME);
                params.append("GENRE_ID", this.GENRE_ID);
                params.append("GOAL_DATE", this.GOAL_DATE);
                params.append("GOAL_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/GOAL_FORM/`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
const GOAL_FORM_UPDATE = {
    path: "/GOAL_FORM/:GOAL_ID",
    component: {
        template: "#GOAL_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                GOAL_ID: null,
                GOAL_NAME: null,
                GENRE_ID: null,
                GOAL_DATE: null,
                VISIBLESTATUS: null,
                values_GENRE: [
                    []
                ],
                button_name: "更新",
                title: "目標フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/GOAL_FORM/${this.$route.params.GOAL_ID}`)
                    .then(res => {
                        this.GOAL_ID = res.data.values[0][0];
                        this.GOAL_NAME = res.data.values[0][1];
                        this.GENRE_ID = res.data.values[0][2];
                        this.GOAL_DATE = res.data.values[0][3];
                        this.VISIBLESTATUS = res.data.values[0][4];
                        this.values_GENRE = res.data.values_GENRE;
                        console.log(res);
                    })
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GOAL_NAME", this.GOAL_NAME);
                params.append("GENRE_ID", this.GENRE_ID);
                params.append("GOAL_DATE", this.GOAL_DATE);
                params.append("GOAL_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/GOAL_FORM/${this.$route.params.GOAL_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};

export { GOAL_TOP, GOAL_FORM, GOAL_FORM_UPDATE, GOAL_TOP_DEL, }