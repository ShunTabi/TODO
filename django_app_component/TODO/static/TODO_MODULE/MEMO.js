"use strict";
const MEMO_TOP = {
    path: "/MEMO_TOP",
    component: {
        template: "#MEMO_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "メモ一覧",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get("http://192.168.10.100:8080/TODO/MEMO_TOP/")
                    .then(res => {
                        this.values = res.data.values;
                        console.log(this.values)
                    })
            },
        },
        created: function () {
            this.axios_GET();
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
                TODO_NAME: null,
                MEMO_NOTE: null,
                MEMO_DATE: null,
                values_TODO: [[]],
                button_name: "登録",
                title: "メモフォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get("http://192.168.10.100:8080/COM/NOW_TIME/")
                    .then(res => {
                        this.MEMO_DATE = res.data.values;
                    });
                axios.get("http://192.168.10.100:8080/TODO/MEMO_FORM/")
                    .then(res => {
                        this.values_TODO = res.data.values_TODO;
                    });
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("TODO_NAME", this.TODO_NAME);
                params.append("MEMO_NOTE", this.MEMO_NOTE);
                params.append("MEMO_DATE", this.MEMO_DATE);
                axios.post("http://192.168.10.100:8080/TODO/MEMO_FORM/", params)
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
                TODO_NAME: null,
                MEMO_NOTE: null,
                MEMO_DATE: null,
                values_TODO: [[]],
                button_name: "更新",
                title: "メモフォーム",
            }
        },
        methods: {
            axios_GET: function () {
                axios.get(`http://192.168.10.100:8080/TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`)
                    .then(res => {
                        this.MEMO_ID = res.data.values[0][0];
                        this.TODO_NAME = res.data.values[0][1];
                        this.MEMO_NOTE = res.data.values[0][2];
                        this.MEMO_DATE = res.data.values[0][3];
                        this.values_TODO = res.data.values_TODO;
                    })
            },
            axios_POST: function () {
                const params = new URLSearchParams();
                params.append("MEMO_ID", this.MEMO_ID);
                params.append("TODO_NAME", this.TODO_NAME);
                params.append("MEMO_NOTE", this.MEMO_NOTE);
                params.append("MEMO_DATE", this.MEMO_DATE);
                axios.post(`http://192.168.10.100:8080/TODO/MEMO_FORM/${this.$route.params.MEMO_ID}`, params)
                    .then(res => { })
            },
        },
        created: function () {
            this.axios_GET();
        }
    }
}
const MEMO_TOP_DEL = {
    path: "/MEMO_TOP_DEL",
    component: {
        template: "#MEMO_TOP",
        delimiters: ["[[", "]]"],
        data: function () {
            return {
                values: null,
                title: "メモ一覧_削除",
            }
        },
        // methods: {
        //     axios_GET: function () {
        //         axios.get("http://192.168.10.100:8080/TODO/TODO_TOP_DEL/")
        //             .then(res => {
        //                 this.values = res.data.values;
        //                 console.log(this.values)
        //             })
        //     },
        // },
        created: function () {
        }
    }
};

export { MEMO_TOP, MEMO_FORM, MEMO_FORM_UPDATE, MEMO_TOP_DEL }