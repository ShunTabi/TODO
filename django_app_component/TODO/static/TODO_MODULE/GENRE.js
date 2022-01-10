"use strict";
//インポート
import { sql_limit, url } from "./conf.js";
//コンポーネント
const GENRE_TOP = {
    path: "/GENRE_TOP/:PAGE",
    component: {
        template: "#GENRE_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                page_max: null,
                title: "種別一覧",
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/GENRE_TOP/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/GENRE_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/GENRE_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
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

const GENRE_TOP_DEL = {
    path: "/GENRE_TOP_DEL/:PAGE",
    component: {
        template: "#GENRE_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "種別一覧_削除",
                page_max: null,
                nav_menu: false,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/GENRE_TOP_DEL/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                    })
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/GENRE_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/GENRE_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
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
const GENRE_FORM = {
    path: "/GENRE_FORM",
    component: {
        template: "#GENRE_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                GENRE_ID: null,
                GENRE_NAME: null,
                GENRE_DATE: null,
                VISIBLESTATUS: 0,
                button_name: "登録",
                title: "種別フォーム",
                values: null,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}COM/NOW_TIME/`)
                    .then(res => {
                        this.GENRE_DATE = res.data.values;
                    });
                axios.get(`${url}TODO/GENRE_TOP/1`)
                    .then(res => {
                        this.values = res.data.values;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("GENRE_DATE", this.GENRE_DATE);
                params.append("GENRE_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/GENRE_FORM/`, params)
                    .then(res => { this.axios_GET() });
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
const GENRE_FORM_UPDATE = {
    path: "/GENRE_FORM/:GENRE_ID",
    component: {
        template: "#GENRE_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                GENRE_ID: null,
                GENRE_NAME: null,
                GENRE_DATE: null,
                VISIBLESTATUS: null,
                button_name: "更新",
                title: "種別フォーム",
                values: null,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/GENRE_FORM/${this.$route.params.GENRE_ID}`)
                    .then(res => {
                        this.GENRE_ID = res.data.values[0][0];
                        this.GENRE_NAME = res.data.values[0][1];
                        this.GENRE_DATE = res.data.values[0][2];
                        this.VISIBLESTATUS = res.data.values[0][3];
                    });
                axios.get(`${url}TODO/GENRE_TOP/1`)
                    .then(res => {
                        this.values = res.data.values;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GENRE_ID", this.GENRE_ID);
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("GENRE_DATE", this.GENRE_DATE);
                params.append("GENRE_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/GENRE_FORM/${this.$route.params.GENRE_ID}`, params)
                    .then(res => { this.axios_GET() });
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
export { GENRE_TOP, GENRE_FORM, GENRE_FORM_UPDATE, GENRE_TOP_DEL }