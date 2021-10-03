"use strict";
const TODO_TOP = {
    path: "/TODO_TOP/:PAGE",
    component: {
        template: "#TODO_TOP",
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
                axios.get(`http://192.168.10.100:8080/TODO/TODO_TOP/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / 9);
                    })
            },
            PAGE_BUTTON: function(tg) {
                this.$router.push(`/TODO_TOP/${parseInt(this.$route.params.PAGE) + tg}`);
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
const TODO_FORM = {
    path: "/TODO_FORM",
    component: {
        template: "#TODO_FORM",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                TODO_ID: null,
                TODO_NAME: null,
                GENRE_NAME: null,
                PRIOR_NAME: null,
                TODO_STARTDATE: null,
                TODO_ENDDATE: null,
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
                        this.TODO_STARTDATE = res.data.values;
                        this.TODO_ENDDATE = res.data.values;
                    });
                axios.get("http://192.168.10.100:8080/TODO/TODO_FORM/")
                    .then(res => {
                        this.values_GENRE = res.data.values_GENRE;
                        this.values_PRIOR = res.data.values_PRIOR;
                    });
            },
            axios_POST: function() {
                const params = new URLSearchParams();
                params.append("TODO_NAME", this.TODO_NAME);
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("PRIOR_NAME", this.PRIOR_NAME);
                params.append("TODO_STARTDATE", this.TODO_STARTDATE);
                params.append("TODO_ENDDATE", this.TODO_ENDDATE);
                console.log(params);
                axios.post(`http://192.168.10.100:8080/TODO/TODO_FORM/`, params)
                    .then(res => {})
            },
        },
        created: function() {
            this.axios_GET();
        }
    }
};
const TODO_FORM_UPDATE = {
    path: "/TODO_FORM/:TODO_ID",
    component: {
        template: "#TODO_FORM",
        delimiters: ["[[", "]]"],
        data: function() {
            return {
                TODO_ID: null,
                TODO_NAME: null,
                GENRE_NAME: null,
                PRIOR_NAME: null,
                TODO_STARTDATE: null,
                TODO_ENDDATE: null,
                values_GENRE: [
                    []
                ],
                values_PRIOR: [
                    []
                ],
                button_name: "更新",
                title: "作業フォーム",
            }
        },
        methods: {
            axios_GET: function() {
                axios.get(`http://192.168.10.100:8080/TODO/TODO_FORM/${this.$route.params.TODO_ID}`)
                    .then(res => {
                        this.TODO_ID = res.data.values[0][0];
                        this.TODO_NAME = res.data.values[0][1];
                        this.GENRE_NAME = res.data.values[0][2];
                        this.PRIOR_NAME = res.data.values[0][3];
                        this.TODO_STARTDATE = res.data.values[0][4];
                        this.TODO_ENDDATE = res.data.values[0][5];
                        this.values_GENRE = res.data.values_GENRE;
                        this.values_PRIOR = res.data.values_PRIOR;
                    })
            },
            axios_POST: function() {
                const params = new URLSearchParams();
                params.append("TODO_ID", this.TODO_ID);
                params.append("TODO_NAME", this.TODO_NAME);
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("PRIOR_NAME", this.PRIOR_NAME);
                params.append("TODO_STARTDATE", this.TODO_STARTDATE);
                params.append("TODO_ENDDATE", this.TODO_ENDDATE);
                axios.post(`http://192.168.10.100:8080/TODO/TODO_FORM/${this.$route.params.TODO_ID}`, params)
                    .then(res => {})
            },
        },
        created: function() {
            this.axios_GET();
        }
    }
}
const TODO_TOP_DEL = {
    path: "/TODO_TOP_DEL/:PAGE",
    component: {
        template: "#TODO_TOP",
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
                axios.get(`http://192.168.10.100:8080/TODO/TODO_TOP_DEL/${this.$route.params.PAGE}`)
                    .then(res => {
                        this.values = res.data.values;
                        this.page_max = Math.ceil(res.data.values_COUNT / 9);
                    })
            },
            PAGE_BUTTON: function(tg) {
                this.$router.push(`/TODO_TOP_DEL/${parseInt(this.$route.params.PAGE) + tg}`);
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

export { TODO_TOP, TODO_FORM, TODO_FORM_UPDATE, TODO_TOP_DEL }