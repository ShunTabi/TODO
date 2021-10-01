"use strict";
const GENRE_TOP = {
    path: "/GENRE_TOP",
    component: {
        template: "#GENRE_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "種別一覧",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get("http://192.168.10.100:8080/TODO/GENRE_TOP/")
                    .then(res => {
                        this.values = res.data.values;
                    })
            },
        },
        created: function () {
            this.axios_GET();
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
                button_name: "登録",
                title: "種別フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get("http://192.168.10.100:8080/COM/NOW_TIME/")
                    .then(res => {
                        this.GENRE_DATE = res.data.values;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("GENRE_DATE", this.GENRE_DATE);
                axios.post(`http://192.168.10.100:8080/TODO/GENRE_FORM/`, params)
                    .then(res => { })
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
                button_name: "更新",
                title: "種別フォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`http://192.168.10.100:8080/TODO/GENRE_FORM/${this.$route.params.GENRE_ID}`)
                    .then(res => {
                        this.GENRE_ID = res.data.values[0][0];
                        this.GENRE_NAME = res.data.values[0][1];
                        this.GENRE_DATE = res.data.values[0][2];
                    })
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("GENRE_ID", this.GENRE_ID);
                params.append("GENRE_NAME", this.GENRE_NAME);
                params.append("GENRE_DATE", this.GENRE_DATE);
                axios.post(`http://192.168.10.100:8080/TODO/GENRE_FORM/${this.$route.params.GENRE_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};

const GENRE_TOP_DEL = {
    path: "/GENRE_TOP_DEL",
    component: {
        template: "#GENRE_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "種別一覧_削除",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get("http://192.168.10.100:8080/TODO/GENRE_TOP_DEL/")
                    .then(res => {
                        this.values = res.data.values;
                    })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
};
export { GENRE_TOP, GENRE_FORM, GENRE_FORM_UPDATE, GENRE_TOP_DEL }