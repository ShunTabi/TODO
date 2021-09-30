"use strict";
//インポート
import { GENRE_TOP, GENRE_FORM, GENRE_FORM_UPDATE, GENRE_DEL } from "./TODO_MODULE/GENRE.js"
import { TODO_TOP, TODO_FORM, TODO_FORM_UPDATE, TODO_DEL } from "./TODO_MODULE/TODO.js"
//ルータ
const router = new VueRouter({
    routes: [
        //GENRE
        GENRE_TOP, GENRE_FORM, GENRE_FORM_UPDATE,
        //TODO
        TODO_TOP, TODO_FORM, TODO_FORM_UPDATE
    ]
});
//APP
const app = new Vue({
    el: "#app",
    router: router,
    created: function () {
    }
});