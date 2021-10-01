"use strict";
//インポート
import { GENRE_TOP, GENRE_FORM, GENRE_FORM_UPDATE, GENRE_TOP_DEL } from "./TODO_MODULE/GENRE.js"
import { TODO_TOP, TODO_FORM, TODO_FORM_UPDATE, TODO_TOP_DEL } from "./TODO_MODULE/TODO.js"
import { MEMO_TOP, MEMO_FORM, MEMO_FORM_UPDATE, MEMO_TOP_DEL } from "./TODO_MODULE/MEMO.js"
//ルータ
const router = new VueRouter({
    routes: [
        //GENRE
        GENRE_TOP, GENRE_FORM, GENRE_FORM_UPDATE, GENRE_TOP_DEL,
        //TODO
        TODO_TOP, TODO_FORM, TODO_FORM_UPDATE, TODO_TOP_DEL,
        //MEMO
        MEMO_TOP, MEMO_FORM, MEMO_FORM_UPDATE, MEMO_TOP_DEL
    ]
});
//APP
const app = new Vue({
    el: "#app",
    router: router,
    created: function () {
    }
});