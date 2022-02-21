"use strict";
// const default_url = "http://localhost:8080/",
const default_url = "http://192.168.10.100:8080/",
    sec = 200,
    par_null = "undefined",
    len_search_key = 10,
    mes_placeholder = `${String(len_search_key)}字まで`,
    len_DAYOFWEEK = 3,
    len_integer = 4,
    isShow = false,
    today = new Date(),
    today_year = today.getFullYear(),
    today_month = today.getMonth() + 1,
    today_date = today.getDate(),
    values_nowtime = `${today_year.toString().padStart(4, "0")}-${today_month.toString().padStart(2, "0")}-${today_date.toString().padStart(2, "0")}`,
    values_nowtime7 = `${today_year.toString().padStart(4, "0")}-${today_month.toString().padStart(2, "0")}-${(today_date + 7).toString().padStart(2, "0")}`,
    button_names = ["登録", "修正", "削除"],
    Lancher_header = [
        "目標",
        "作業",
        "課題",
        "メモ",
        "種別",
        "管理",
    ],
    Lancher_detail_name = [
        "一覧",
        "フォーム",
        "全体(一覧、フォーム)",
        "進捗",
        "ゴミ箱",
    ],
    Lancher_detail = [
        [
            //目標
            [Lancher_header[0] + Lancher_detail_name[2], "/GOAL/2/1"],//全体
            [Lancher_header[0] + Lancher_detail_name[0], "/GOAL/0/1"],//一覧
            [Lancher_header[0] + Lancher_detail_name[1], "/GOAL/1/1"],//フォーム
        ],
        [
            //作業
            [Lancher_header[1] + Lancher_detail_name[2], `/TODO_HEADER/2/1/${par_null}`],
            [Lancher_header[1] + Lancher_detail_name[0], `/TODO_HEADER/0/1/${par_null}`],
            [Lancher_header[1] + Lancher_detail_name[1], `/TODO_HEADER/1/1/${par_null}`],
        ],
        [
            //課題
            [Lancher_header[2] + Lancher_detail_name[2], `/TODO_DETAIL/2/1/${par_null}/${par_null}`],
            [Lancher_header[2] + Lancher_detail_name[0], `/TODO_DETAIL/0/1/${par_null}/${par_null}`],
            [Lancher_header[2] + Lancher_detail_name[1], `/TODO_DETAIL/1/1/${par_null}/${par_null}`],
        ],
        [
            //メモ
            [Lancher_header[3] + Lancher_detail_name[2], `/MEMO/2/1/${par_null}`],
            [Lancher_header[3] + Lancher_detail_name[0], `/MEMO/0/1/${par_null}`],
            [Lancher_header[3] + Lancher_detail_name[1], `/MEMO/1/1/${par_null}`],
        ],
        [
            //種別
            [Lancher_header[4] + Lancher_detail_name[2], "/GENRE/2/1"],
            [Lancher_header[4] + Lancher_detail_name[0], "/GENRE/0/1"],
            [Lancher_header[4] + Lancher_detail_name[1], "/GENRE/1/1"],
        ],
        [
            //管理
            [Lancher_header[5] + Lancher_detail_name[3], `/TODO_MANAGE/0/1/${values_nowtime}/${values_nowtime7}/${par_null}`],
        ],
    ],
    DAYOFWEEK = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ],
    start_url = `${default_url}TODO/#${Lancher_detail[2][1][1]}`;

export {
    default_url,
    sec,
    start_url,
    button_names,
    Lancher_header,
    Lancher_detail,
    isShow,
    par_null,
    mes_placeholder,
    DAYOFWEEK,
    len_DAYOFWEEK,
    len_integer,
    len_search_key,
    values_nowtime,
    values_nowtime7,
}