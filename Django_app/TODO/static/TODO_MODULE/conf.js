"use strict";
// const default_url = "http://localhost:8080/",
const default_url = "http://192.168.10.100:8080/",
    sec = 200,
    par_null = "undefined",
    len_search_key = 10,
    mes_placeholder = `${String(len_search_key)}字まで`,
    len_charactor = 15,
    len_integer = 4,
    isShow = false,
    button_names = ["登録", "修正", "削除"],
    Lancher_header = ["目標", "作業", "課題", "メモ", "種別"],
    Lancher_detail_name = ["一覧", "フォーム", "全体(一覧、フォーム)", "ゴミ箱"],
    Lancher_detail = [
        [
            //目標
            [Lancher_header[0] + Lancher_detail_name[2], "/GOAL_/2/1"],
            [Lancher_header[0] + Lancher_detail_name[0], "/GOAL_/0/1"],
            [Lancher_header[0] + Lancher_detail_name[1], "/GOAL_/1/1"],
        ],
        [
            //作業
            [Lancher_header[1] + Lancher_detail_name[2], `/TODO_HEADER_/2/1/${par_null}`],
            [Lancher_header[1] + Lancher_detail_name[0], `/TODO_HEADER_/0/1/${par_null}`],
            [Lancher_header[1] + Lancher_detail_name[1], `/TODO_HEADER_/1/1/${par_null}`],
        ],
        [
            //課題
            [Lancher_header[2] + Lancher_detail_name[2], `/TODO_DETAIL_/2/1/${par_null}/${par_null}`],
            [Lancher_header[2] + Lancher_detail_name[0], `/TODO_DETAIL_/0/1/${par_null}/${par_null}`],
            [Lancher_header[2] + Lancher_detail_name[1], `/TODO_DETAIL_/1/1/${par_null}/${par_null}`],
        ],
        [
            //メモ
            [Lancher_header[3] + Lancher_detail_name[2], `/MEMO_/2/1/${par_null}`],
            [Lancher_header[3] + Lancher_detail_name[0], `/MEMO_/0/1/${par_null}`],
            [Lancher_header[3] + Lancher_detail_name[1], `/MEMO_/1/1/${par_null}`],
        ],
        [
            //種別
            [Lancher_header[4] + Lancher_detail_name[2], "/GENRE_/2/1"],
            [Lancher_header[4] + Lancher_detail_name[0], "/GENRE_/0/1"],
            [Lancher_header[4] + Lancher_detail_name[1], "/GENRE_/1/1"],
        ],
    ],
    start_url = `${default_url}TODO/#${Lancher_detail[2][2]}`;

export {
    default_url,
    sec,
    start_url,
    button_names,
    Lancher_header,
    Lancher_detail,
    len_charactor,
    len_integer,
    isShow,
    par_null,
    len_search_key,
    mes_placeholder,
}