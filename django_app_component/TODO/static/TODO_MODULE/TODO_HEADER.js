"use strict";
//インポート
import { sql_limit, url } from "./conf.js";
//コンポーネント
const TODO_HEADER_TOP = {
    path: "/TODO_HEADER_TOP/:PAGE",
    component: {
        template: "#TODO_HEADER_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                title: "作業一覧",
                values: null,
                page_max: null,
                nav_menu: false,
                PRIOR_ID: 0,
                GOAL_ID: 0,
                values_GOAL: [[]],
                values_PRIOR: [[]],
            }
        },
        methods: {
            axios_GET: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("PRIOR_ID", this.PRIOR_ID);
                axios.get(`${url}TODO/TODO_HEADER_TOP/${this.$route.params.PAGE}`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                        this.values_GOAL = res.data.values_GOAL;
                        this.values_PRIOR = res.data.values_PRIOR;
                    });
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/TODO_HEADER_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/TODO_HEADER_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
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
const TODO_HEADER_TOP_DEL = {
    path: "/TODO_HEADER_TOP_DEL/:PAGE",
    component: {
        template: "#TODO_HEADER_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "作業一覧_削除",
                page_max: null,
                nav_menu: false,
                PRIOR_ID: 0,
                GOAL_ID: 0,
                values_GOAL: [
                    []
                ],
                values_PRIOR: [
                    []
                ],
            }
        },
        methods: {
            axios_GET: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("PRIOR_ID", this.PRIOR_ID);
                axios.get(`${url}TODO/TODO_HEADER_TOP_DEL/${this.$route.params.PAGE}`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / sql_limit);
                        this.values_GOAL = res.data.values_GOAL;
                        this.values_PRIOR = res.data.values_PRIOR;
                    });
            },
            axios_DEL: function (tg) {
                axios.post(`${url}TODO/TODO_HEADER_DEL/${tg}`)
                    .then(res => {
                        this.axios_GET();
                    })
            },
            PAGE_BUTTON: function (tg) {
                this.$router.push(`/TODO_HEADER_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
                this.axios_GET();
            },
            nav_menu_if: function () {
                this.nav_menu = !this.nav_menu;
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
const TODO_HEADER_FORM = {
    path: "/TODO_HEADER_FORM",
    component: {
        template: "#TODO_HEADER_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                TODO_HEADER_ID: null,
                TODO_HEADER_NAME: null,
                PRIOR_ID: null,
                GOAL_ID: null,
                TODO_HEADER_STARTDATE: null,
                TODO_HEADER_ENDDATE: null,
                VISIBLESTATUS: 0,
                values_PRIOR: [[]],
                values_GOAL: [[]],
                button_name: "登録",
                title: "作業フォーム",
                values: null,
                page_max: null,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}COM/NOW_TIME/`)
                    .then(res => {
                        this.TODO_HEADER_STARTDATE = res.data.values;
                        this.TODO_HEADER_ENDDATE = res.data.values;
                    });
                axios.get(`${url}TODO/TODO_HEADER_FORM/`)
                    .then(res => {
                        this.values_PRIOR = res.data.values_PRIOR;
                        this.values_GOAL = res.data.values_GOAL;
                    });
                const params = new URLSearchParams();
                params.append("GOAL_ID", 0);
                params.append("PRIOR_ID", 0);
                axios.get(`${url}TODO/TODO_HEADER_TOP/1`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("PRIOR_ID", this.PRIOR_ID);
                params.append("TODO_HEADER_STARTDATE", this.TODO_HEADER_STARTDATE);
                params.append("TODO_HEADER_ENDDATE", this.TODO_HEADER_ENDDATE);
                params.append("TODO_HEADER_VISIBLESTATUS", this.VISIBLESTATUS);
                console.log(params);
                axios.post(`${url}TODO/TODO_HEADER_FORM/`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
const TODO_HEADER_FORM_UPDATE = {
    path: "/TODO_HEADER_FORM/:TODO_HEADER_ID",
    component: {
        template: "#TODO_HEADER_FORM",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                TODO_HEADER_ID: null,
                TODO_HEADER_NAME: null,
                PRIOR_ID: null,
                GOAL_ID: null,
                TODO_HEADER_STARTDATE: null,
                TODO_HEADER_ENDDATE: null,
                VISIBLESTATUS: null,
                values_PRIOR: [[]],
                values_GOAL: [[]],
                button_name: "更新",
                title: "作業フォーム",
                values: null,
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`${url}TODO/TODO_HEADER_FORM/${this.$route.params.TODO_HEADER_ID}`)
                    .then(res => {
                        this.TODO_HEADER_ID = res.data.values[0][0];
                        this.GOAL_ID = res.data.values[0][1];
                        this.TODO_HEADER_NAME = res.data.values[0][2];
                        this.PRIOR_ID = res.data.values[0][3];
                        this.TODO_HEADER_STARTDATE = res.data.values[0][4];
                        this.TODO_HEADER_ENDDATE = res.data.values[0][5];
                        this.VISIBLESTATUS = res.data.values[0][6];
                        this.values_PRIOR = res.data.values_PRIOR;
                        this.values_GOAL = res.data.values_GOAL;
                    });
                const params = new URLSearchParams();
                params.append("GOAL_ID", 0);
                params.append("PRIOR_ID", 0);
                axios.get(`${url}TODO/TODO_HEADER_TOP/1`, { "params": params })
                    .then(res => {
                        this.values = res.data.values;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GOAL_ID", this.GOAL_ID);
                params.append("TODO_HEADER_NAME", this.TODO_HEADER_NAME);
                params.append("PRIOR_ID", this.PRIOR_ID);
                params.append("TODO_HEADER_STARTDATE", this.TODO_HEADER_STARTDATE);
                params.append("TODO_HEADER_ENDDATE", this.TODO_HEADER_ENDDATE);
                params.append("TODO_HEADER_VISIBLESTATUS", this.VISIBLESTATUS);
                axios.post(`${url}TODO/TODO_HEADER_FORM/${this.$route.params.TODO_HEADER_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
}

export { TODO_HEADER_TOP, TODO_HEADER_FORM, TODO_HEADER_FORM_UPDATE, TODO_HEADER_TOP_DEL, }