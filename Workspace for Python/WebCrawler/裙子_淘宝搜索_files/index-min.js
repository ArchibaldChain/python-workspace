try{!function(){if(!window.__aawd__622__&&(window.__aawd__622__=99,"undefined"!=typeof KISSY)){KISSY.add("GG39.u-u",function(a,b){function c(a){return encodeURIComponent(a)}function d(a){try{return decodeURIComponent(a)}catch(b){}return""}function e(a,b){var c={};if("object"==typeof a&&"object"==typeof b&&a&&b){for(var d in b)void 0===a[d]?c[d]=b[d]:c[d]=a[d];return c}}function f(){var a=location.href.substring(location.protocol.length+2,location.href.indexOf("?")>-1?location.href.indexOf("?"):location.href.length);return"/"===a.charAt(a.length-1)&&(a=a.substring(0,a.length-1)),a}function g(a){return a?(a+="",k(a,"http://")?a=a.substring(7):k(a,"https://")&&(a=a.substring(8)),a.indexOf("/")>-1&&(a=a.substring(0,a.indexOf("/"))),a):""}function h(a,b){if(!(b&&b instanceof Array))return!1;if(Array.prototype.indexOf)return b.indexOf(a)>-1;for(var c=0,d=b.length;d>c;c++)if(b[c]===a)return!0;return!1}function i(a,b){if(!(b&&b instanceof Array&&"function"==typeof a))return null;for(var c=0;c<b.length;c++)if(a(b[c]))return b[c];return null}function j(a,b){if(a instanceof Array&&b instanceof Array){var c;for(c=0;c<b.length;c++)a.push(b[c])}}function k(a,b){return"string"!=typeof a||"string"!=typeof b?!1:a.substring(0,b.length)===b}function l(a,b){return"string"!=typeof a||"string"!=typeof b?!1:a.substring(a.length-b.length)===b}function m(a,b){if(Object.create)return Object.create(a,b);var c=function(){};return c.prototype=a,new c}function n(a,b){a.prototype=m(b.prototype),a.prototype.constructor=a}function o(){var a,b=navigator.userAgent.toLowerCase(),c=b.indexOf("msie")>-1,d=document,e=location.pathname.split("/");e[e.length-1]="";var f,g=encodeURIComponent(e.join("/"));try{f=window.localStorage}catch(h){}if(f)return a=window.localStorage,{setkey:function(b,c){try{a.setItem(b,c)}catch(d){return!1}return!0},getkey:function(b){try{return a.getItem(b)}catch(c){return}}};if(c){if(a=d.getElementById("_tanxssp_userdata"),!a){a=d.createElement("input"),a.type="hidden",d.body.insertBefore(a,d.body.firstChild);try{a.addBehavior("#default#userData")}catch(h){}}return{setkey:function(b,c){try{a.load(g),a.setAttribute(b,c),a.save(g)}catch(d){return!1}return!0},getkey:function(b){try{a.load(g)}catch(c){return}return a.getAttribute(b)}}}return{setkey:function(){},getkey:function(){}}}function p(a){if(a=r(a),!a||!a.css)return"unknown";var b="";return a.nodeName&&(b+=a.nodeName()),a.attr("id")&&(b+="|id="+a.attr("id")),a.attr("data-id")&&(b+="|data-id="+a.attr("data-id")),a.attr("class")&&(b+="|class="+(b?"|":"")+a.attr("class")),a.attr("src")&&(b+="|src="+a.attr("src")),a.attr("href")&&(b+="|href="+a.attr("href")),a.attr("style")&&(b+="|style="+a.attr("style")),b||(b="unknown"),b}function q(){return function(){return this}()}var r=b.all;return{YO7:f,YA8:g,inArray:h,findInArray:i,arrayAdd:j,startsWith:k,endsWith:l,encode:c,decode:d,createObjectFromMerge:e,objectCreate:m,inherit:n,getStorage:o,EJ9:p,getGlobalObject:q}},{requires:["node"]}),KISSY.add("GG39.u-l",function(a,b,c,d){function e(){this.alarmCount=0}var f=d.GH18.TL37.NN27.FX28,g=d.GH18.TL37.NN27.RE36,h=["type","href","aa","bb","cc","dd","ee"],i=["type"];return e.prototype.OL12=function(a,d,e){function j(a,d){return k&&!b.inArray(a,i)?c.e(d):d}if(a){this.alarmCount+=1;var k=g;e&&e.RE36===!1&&(k=!1),a.type=(a.type||"other")+f.YU41;var l,m,n=[],o=[];for(l=0;l<h.length;l++)m=h[l],a[m]&&(n.push(m+"="+j(m,b.encode(a[m]))),o.push(m+"="+a[m]));e&&e.FX28&&(f=e.FX28),0!==n.length&&(n=n.join("&"),"undefined"!=typeof goldlog&&goldlog.record(f.KEY,"",n,f.ID))}},e.prototype.hasAlarm=function(){return this.alarmCount>0},e},{requires:["GG39.u-u","GG39.u-e","GG39.c"]}),KISSY.add("GG39.u-e",function(){function a(a){a+="";for(var c,d,e=[],g=0,h=a.length;h>g;g++)c=a.charAt(g),d=b(c),e.unshift(d);return f(e.join(String.fromCharCode(1)))}function b(a){var b=a,e=a.charCodeAt();return b=c(a)?e-"A".charCodeAt()+3:String.fromCharCode(d(a)?+a+"f".charCodeAt():e+1)}function c(a){var b=a.charCodeAt();return b>=65&&90>=b||b>=97&&122>=b}function d(a){var b=a.charCodeAt();return b>=48&&57>=b}function e(a){var b,c,d,e,f,h;for(d=a.length,c=0,b="";d>c;){if(e=255&a.charCodeAt(c++),c==d){b+=g.charAt(e>>2),b+=g.charAt((3&e)<<4),b+="==";break}if(f=a.charCodeAt(c++),c==d){b+=g.charAt(e>>2),b+=g.charAt((3&e)<<4|(240&f)>>4),b+=g.charAt((15&f)<<2),b+="=";break}h=a.charCodeAt(c++),b+=g.charAt(e>>2),b+=g.charAt((3&e)<<4|(240&f)>>4),b+=g.charAt((15&f)<<2|(192&h)>>6),b+=g.charAt(63&h)}return b}function f(a){return e(a)}var g="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";return{e:a}},{requires:[]}),KISSY.add("GG39.c",function(){var a={AX35:"0.3.3"},b={BF14:["www.taobao.com","mclick.simba.taobao.com","click.simba.taobao.com","click.tanx.com","click.mz.simba.taobao.com","click.tz.simba.taobao.com","redirect.simba.taobao.com","rdstat.tanx.com","stat.simba.taobao.com","s.click.taobao.com"],FM15:["a.tbcdn.cn","img01.taobaocdn.com","img02.taobaocdn.com","img03.taobaocdn.com","img04.taobaocdn.com","img07.taobaocdn.com","img08.taobaocdn.com","img1.tbcdn.cn","img2.tbcdn.cn","img3.tbcdn.cn","img.alimama.cn","i.mmcdn.cn","strip.taobaocdn.com","acjstb.aliyun.com","count.taobao.com","g-assets.daily.taobao.net",/\.alicdn\.com$/],CS16:[/\.taobao\.com$/,/\.taobao\.net$/,/\.alicdn\.com$/,/\.tmall\./,/\.mmstat\.com$/,/\.tanx\.com$/,/\.etao\.com$/,/\.alipay\.com$/,/\.alibaba\.com$/,/\.alibaba\.cn$/,/\.aliexpress\.com$/,/\.alibaba-inc\.com$/,/\.laiwang\.com$/,/\.microsoft\.com$/,/\.uc\.cn$/,/\.google\.cn$/,/\.china\.com\.cn$/,/\.alibabagroup\.com$/,/\.1688\.com$/,/\.alimama\.com$/,/\.aliyun\.com$/,/\.yunos\.com$/,/\.aliqin\.cn$/,/\.autonavi\.com$/,/\.xiami\.com$/,/\.taobaocdn\.com$/,/\.umeng\.com$/,/\.kanbox\.com$/,/\.ttpod\.com$/,/\.ttpod\.com$/,/\.ppaaol\.com$/,/\.gov\.cn$/,/\.knet\.cn$/,/\.theclimategroup\.org\.cn$/,/\.net\.cn$/,/^javascript:.*/]},c={"www.taobao.com":{AdLink:[".promo-bd a"],II32:[".promo-bd img"],AQ33:[".promo-bd img"],id:"ti"},"www.tmall.com":{},"s.taobao.com/search|s.daily.taobao.net/search":{AdLink:["#J_shopkeeper a"],II32:["#J_shopkeeper img"],AQ33:["#J_shopkeeper img"],id:"ts"},"list.tmall.com/search_product.htm":{},"item.taobao.com/item.htm":{},"detail.tmall.com/item.htm":{}},d={TL37:{VO19:[3,6,9],LC20:2e3,IC21:.001,MV10:!1,NN27:{RE36:!0,FX28:{YU41:"_"+a.AX35.replace(/\./g,"_"),KEY:"/tanx.560",ID:"H1733390"}}},II22:{},NE23:{},RL24:{},YK25:{MV10:!0},WD26:{VO19:[4],MV10:!0,IC21:1,NN27:{RE36:!1,FX28:{YU41:"_"+a.AX35.replace(/\./g,"_"),KEY:"/tanx.987",ID:"H1733418"}}}};return{GG39_MR38:a,RULES_MR38:c,NJ13_MR38:b,GH18:d}},{requires:[]}),KISSY.add("GG39.s-dbc",function(a,b,c,d){function e(){this.scanCounter=1,this.disabled=!0,("WD26"===this.key||"function"==typeof Object.create)&&this.key&&void 0!==c.GH18[this.key]&&(this.JP30orMY42=d.createObjectFromMerge(c.GH18[this.key],c.GH18.TL37),Math.random()<1-this.JP30orMY42.IC21||this.JP30orMY42.MV10&&(this.rulesMY42=c.RULES_MR38,this.OL43MY42=c.NJ13_MR38,this.disabled=!1))}var f,g=function(){},h=c.RULES_MR38,i={};return e.init=function(a){a=a||{},f=a.logger||g},e.ER29=function(a,b){var c,e;for(e in b)if(c=e.split("|"),d.inArray(a,c))return b[e];return null},e.prototype.OL12=function(a,b,c){var d=a.type;(!i[d]||c&&c.forceSendLog)&&(i[d]=1,a&&a.type&&this.pageId&&(a.type+="_"+this.pageId),f&&f.OL12.call(this,a,b,this.JP30orMY42.NN27))},e.prototype.bo=function(a){if(this.disabled!==!0){this.scanCounter++;var b,c,g=d.YO7(),i=e.ER29(g,h);if(i){this.pageId=i.id;for(c in i)if(i.hasOwnProperty(c)){var j=this["JP30"+c];if("function"==typeof j){var k=i&&i[c];if(k&&k.length)for(b=0;b<k.length;b++)j.call(this,k[b])}}}this.JP30&&this.JP30(),this.collect&&this.collect(),!f.hasAlarm()}},e.prototype.getMY42=function(){return this.JP30orMY42},e.prototype.isDisabled=function(){return this.disabled},e},{requires:["node","GG39.c","GG39.u-u"]}),KISSY.add("GG39.s-dcc",function(a,b,c,d){function e(){this.key="II22",this.__lock_JP30AQ33=0,d.apply(this,arguments)}function f(a,c){for(var d=b.one(a),e=b.one(c),f=!1;d;){if(d.equals(e)){f=!0;break}d=d.parent()}return f}function g(a){var b,c,d,e=+a.left,f=+a.top,g=+a.width,h=+a.height,i=[],j=3,k=[[e+j,f+j],[e+g-j,f+j],[e+j,f+h-j],[e+g-j,f+h-j],[e+g/2,f+h/2]];if(!e||!f||!h||!g||10>h||10>g)return[];for(b=0;b<k.length;b++)d=null,c=k[b],c[0]&&c[1]&&(d=document.elementFromPoint(c[0],c[1])),d&&i.push(d);return i}function h(a){var c,d,e=b.one(a),h=e.offset(),i=h.left||0,j=h.top||0,k=e.width(),l=e.height(),m=g({left:i,top:j,width:k,height:l}),n=[];for(c=0;c<m.length;c++)d=m[c],f(d,a)||null===d||n.push(d);return n}var i=b.all;return c.inherit(e,d),e.prototype.JP30AQ33=function(a){var b,d=("string"==typeof a?a:c.EJ9(a),i(a)),e=this,f=[],g=[];if(d&&0!==d.length){if(d&&d.length>1&&e.__lock_JP30AQ33++<this.JP30orMY42.LC20)return void d.each(function(a){e.JP30AQ33(a)});d.each(function(a){var b=h(a);if(b&&b.length){{c.EJ9(a)}c.arrayAdd(g,b)}}),g.length;var j;for(b=0;b<g.length;b++)j=i(g[b]),f.push(c.EJ9(j));f.length&&this.OL12({type:"concover",href:f.join("_")})}},e},{requires:["node","GG39.u-u","GG39.s-dbc"]}),KISSY.add("GG39.s-dcd",function(a,b,c,d){function e(){this.key="NE23",this.__lock_JP30AQ33=0,d.apply(this,arguments)}function f(a){var b;return b="none"===a.css("display")?"display":"hidden"===a.css("visibility")?"visibility":0===parseInt(a.css("width"))||0===parseInt(a.css("height"))?"width":null}var g=b.all;return c.inherit(e,d),e.prototype.JP30AQ33=function(a){var b=("string"==typeof a?a:c.EJ9(a),this),d=g(a);if(d&&d.length>1&&b.__lock_JP30AQ33++<this.JP30orMY42.LC20)return void d.each(function(a){b.JP30AQ33(a)});var e,h=0,i=[];if(d&&0!==d.length){for(;d.getDOMNode()!==document.body&&h++<100;){if(e=f(d)){var j=c.EJ9(d);i.push(e),i.push(j)}d=d.parent()}i.length&&this.OL12({type:"conhide",href:i.join("_")})}},e},{requires:["node","GG39.u-u","GG39.s-dbc"]}),KISSY.add("GG39.s-dcm",function(a,b,c){function d(){this.key="RL24",c.apply(this,arguments)}return b.inherit(d,c),d},{requires:["GG39.u-u","GG39.s-dbc"]}),KISSY.add("GG39.s-dle",function(a,b,c,d){function e(){this.key="YK25",d.apply(this,arguments),g=this.OL43MY42}function f(a,b){if(void 0===a||"undefined"===a||c.startsWith(a,"//"))return!0;var d,e=c.YA8(a),f=0;d="img.src"===b?g.FM15:g.CS16;for(var h,i=d.length,j=!1;i>f;f++)if(h=d[f],"string"==typeof h&&e.indexOf(h)>-1||h instanceof RegExp&&h.test(e)){j=!0;break}return j}var g,h=b.all;return c.inherit(e,d),e.prototype.JP30AdLink=function(a){var b=h(a),d=[];d.push(window.location.href),b&&0!==b.length&&(b.each(function(b){var e,g=b.attr("href");f(g)||(e=c.EJ9(b.parent()),d.push(a),d.push(e),d.push(g))}),d.length>1&&this.OL12({type:"adlink",href:d.join("|")}))},e.prototype.JP30II32=function(a){var b=h(a),d=[];d.push(window.location.href),b&&0!==b.length&&(b.each(function(b){var e,g=b.attr("src");f(g,"img.src")||(d.push(a),e=c.EJ9(b.parent()),d.push(e),d.push(g))}),d.length>1&&this.OL12({type:"imglink",href:d.join("|")}))},e},{requires:["node","GG39.u-u","GG39.s-dbc"]});var a=a||{};a.AY40=[{p:0,s:1,t:(new Date).getTime()}],a._c=function(b,c,d,e){function f(a,b){if(!(b&&b instanceof Array&&"function"==typeof a))return null;for(var c=0;c<b.length;c++)if(a(b[c]))return b[c];return null}b+="";var g=!1;if(void 0!==b&&void 0!==c){var h=f(function(a){return a.p+""==b+""},a.AY40);h&&+c<=+h.s&&a.reload&&(a.reload(),g=!0),a.AY40.push({p:b,s:c,t:(new Date).getTime(),rn:d,c:e})}},window.__ocbad__=a,KISSY.add("GG39.s-ocbad",function(b,c,d,e,f){function g(){this.key="WD26",f.apply(this,arguments),i=this}var h=["p","s","t"],i=null;return e.inherit(g,f),g.prototype.collect=function(b){b=b||{},b.forceSendLog=!0;var c,d,e,f,g,i=this,j=[],k=a.AY40,l=b&&b.isSup===!0?!0:!1;for(f=0;f<k.length;f++){d=[],void 0===e&&(e=k[f].rn),void 0===g&&(g=k[f].c),c=k[f];for(var m=0;m<h.length;m++)d.push(c[h[m]]);j.push(d.join(","))}j.length&&(i.OL12({type:l?"ocbad_sup":"ocbad",aa:e,bb:j.join("|"),cc:g},void 0,b),a.AY40.sent=!0,l||(i.supSendTimer=setTimeout(function(){i.collect({isSup:!0}),i.supSendTimer=null,a.AY40.supSent=!0},1e3*i.JP30orMY42.VO19[0])))},a.reload=function(){i&&(i.supSendTimer&&(clearTimeout(i.supSendTimer),i.supSendTimer=null),a.AY40.sent||i.collect()),a.AY40=[{p:-1,s:1,t:(new Date).getTime()}],i&&setTimeout(function(){i.collect()},1e3*i.JP30orMY42.VO19[0])},g},{requires:["node","json","GG39.u-u","GG39.s-dbc"]}),KISSY.add("GG39.s-m",function(a,b,c,d,e){function f(){}var g,h=arguments,i=5;return f.prototype.bo=function(a){g=a||{};var b=[].slice.call(h).slice(i);d.init({logger:new c});var e,f,j,k,l,m;for(e=0;e<b.length;e++)if(k=new b[e],!k.isDisabled())for(l=k.getMY42(),m=l.VO19,j=m.length,f=0;j>f;f++)!function(a,b,c){setTimeout(function(){a.bo(1e3*c[b])},1e3*c[b])}(k,f,m)},f},{requires:["node","GG39.u-l","GG39.s-dbc","GG39.c","GG39.s-dcc","GG39.s-dcd","GG39.s-dcm","GG39.s-dle","GG39.s-ocbad"]}),KISSY.use(["GG39.s-m","GG39.c"],function(a,b,c){(new b).bo()})}}()}catch(ex){}

KISSY.add("p4p", function(S) {
    return function(cfg) {

        S.use("json", function() {

            window.MBOX = {}
            document.createElement("tbcc")
            if (!S.one("#J_shopkeeper")) {
                S.one("[id$='p4pRight']").html('<div class="m-p4p"><div id="J_shopkeeper" style="height: 2000px;"></div></div>')
                S.one("[id$='p4pBottom']").html('<div class="m-p4p"><div id="J_shopkeeper_bottom"><div class="loading">加载中...</div></div></div>')
            }
            S.one("#J_shopfeature") && S.one("#J_shopfeature").remove()
            var p4pconfig = cfg.p4pconfig
            MBOX.p4pconfig = p4pconfig
            var data = S.JSON.parse(cfg.p4pdata || 0)
            var keyword = p4pconfig.keywordGBK
            var frontcatid = p4pconfig.frontcatid
            var pageNum = p4pconfig.pageNum || 1
            var b2b_show = p4pconfig.b2b_show
            var rn = p4pconfig.rn
            var pageName = p4pconfig.pageName

            var rightArgs = {
                type: "right",
                width: p4pconfig.rightWidth || getWidth("right"),
                id: "J_shopkeeper",
                qs: [{
                    pid: "420434_1006",
                    keyword: keyword,
                    catid: frontcatid,
                    count: 16,
                    se: rn,
                    offset: (pageNum - 1) * (b2b_show ? 16 : 21)
                }]
            }

            var bottomArgs = {
                type: "bottom",
                // width: p4pconfig.pageWidth || getWidth("bottom"),
                id: "J_shopkeeper_bottom",
                qs: [{
                    pid: "420435_1006",
                    keyword: keyword,
                    frcatid: frontcatid,
                    offset: (pageNum - 1) * 21 + 16
                }, {
                    pid: p4pconfig.source === "lsrp" ? "430355_1006" : p4pconfig.source === "festival" ? "430360_1006" : "419110_1006",
                    keyword: keyword,
                    catid: frontcatid
                }]
            }

            if(data && data.righttop && data.righttop.data && data.righttop.data.ds1 && data.righttop.data.ds1[0] && data.righttop.data.ds1[0].adList && data.righttop.data.ds1[0].adList[0]) {
                var ad = data.righttop.data.ds1[0].adList[0]
                var width = p4pconfig.rightWidth

                if (ad.height === 235) {
                    if (pageName === "spulist" || pageName === "spudetail") {
                        MBOX.notitle = true
                    }
                }

                MBOX.righttopRatio = (ad.height - 55) / ad.width
                var height = width * MBOX.righttopRatio + (MBOX.notitle ? 0 : 55)

                var src = ad.iframe_src.replace(/^http:/, "https:")
                if (MBOX.notitle) src = src + "&notitle=1"

                if(ad.height == 600 && src.indexOf("tianmu=1") > -1) {
                    MBOX.qiqiaoban = true
                    height = 600
                    S.one("#J_shopkeeper").parent().css("margin-top", 0)
                    if (S.one(".m-shopstar")) S.one(".m-shopstar").css("font-size", 0)
                }

                S.one("#J_shopkeeper").before('<iframe src="' + src + '"id="J_topshop" style="width:' + width + 'px;height:' + height + 'px" border="0" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" allowtransparency="true"></iframe>')
            }

            if(data && isValidTemplateData(data.right)) {
                var logKgbData = Math.floor(Math.random() * 10000) === 8888 ? S.JSON.stringify(data.right.ds1).slice(0, 2000) : ""
                window.__ocbad__ && __ocbad__._c("420434_1006", 3, rn, logKgbData)
                rightArgs.qs[0].pid = data.right.pid
                renderTemplate(S.merge(data.right, rightArgs), removeShopkeeperHeight)
            } else {
                renderTemplate(S.merge({
                    template: "//acc.alicdn.com/tfscom/TB1raeOIVXXXXc6aXXXdutXFXXX.js",
                    creation_path: "2015_8/130027"
                }, rightArgs), removeShopkeeperHeight)
            }

            S.use("datalazyload", function() {
                var J_shopkeeper_bottom = document.getElementById("J_shopkeeper_bottom")
                if(J_shopkeeper_bottom) {
                    var lazyLoad = S.DataLazyload({
                        diff: 800,
                        placeholder: "//assets.alicdn.com/g/s.gif"
                    })
                    lazyLoad.addCallback("#J_shopkeeper_bottom", function() {
                        bottomArgs.width = getWidth("bottom")
                        if(data && isValidTemplateData(data.bottom)) {
                            bottomArgs.qs[0].pid = data.bottom.pid
                            renderTemplate(S.merge(data.bottom, bottomArgs))
                        } else if(data && data.bottom && data.bottom.rstCode === 1 && data.bottom.qs && data.bottom.qs[0]) {
                            bottomArgs.qs[0] = data.bottom.qs[0]
                            renderTemplate(S.merge(data.bottom, bottomArgs))
                        } else {
                            if(b2b_show) { // 出网销宝
                                bottomArgs.qs[0].keywords = keyword
                                renderTemplate(S.merge({
                                    template: "//acc.alicdn.com/tfscom/TB1T6CJJXXXXXbQXFXXdutXFXXX.js",
                                    creation_path: "2015_8/130042"
                                }, bottomArgs), function(success) {
                                    if(!success) {
                                        renderTemplate(S.merge({
                                            template: "//acc.alicdn.com/tfscom/TB1_MntHVXXXXcEXVXXdutXFXXX.js",
                                            creation_path: "2015_5/129617"
                                        }, bottomArgs))
                                    }
                                })
                            } else {
                                renderTemplate(S.merge({
                                    template: "//acc.alicdn.com/tfscom/TB1_MntHVXXXXcEXVXXdutXFXXX.js",
                                    creation_path: "2015_5/129617"
                                }, bottomArgs))
                            }
                        }
                    })
                }
            })

            function removeShopkeeperHeight() {
                var J_shopkeeper = document.getElementById("J_shopkeeper")
                if(J_shopkeeper) {
                    J_shopkeeper.style.height = "auto"
                }
            }

            function isValidTemplateData(data) {
                return data && data.data && data.template && data.creation_path
            }

            function renderTemplate(data, afterRender) {
                var id = data.creation_path
                MBOX[id] = data
                var uid = "c" + id.replace(/[^-a-z0-9]/ig, "-") + "-" + (+new Date())
                var container = document.getElementById(data.id)
                if(container) {
                    container.innerHTML = '<tbcc id="tbcc-c-' + uid + '" style="display:none"><tbcc></tbcc></tbcc>'
                    S.getScript(data.template.replace("http://strip.taobaocdn.com", "//acc.alicdn.com"), function() {
                        _ent.use("cc/show", function(cc) {
                            cc.show(id, uid).on("render", function(_, success) {
                                afterRender && afterRender(success)
                            })
                        })
                    })
                }
            }

            function getWidth(rightOrBottom) {
                var bodyClass = S.one("body").attr("class");
                var widthType = bodyClass ?
                    (bodyClass.match(/(?:range-1-|response-|^w)(\w+)/) || [, "ie6"])[1].toLowerCase() :
                    "normal";
                var widthMapRight = {
                    small: 200,
                    narrow: 200,
                    normal: 240,
                    large: 270,
                    wider: 270,
                    ie6: 230
                };
                var widthMapBottom = {
                    small: 1000,
                    narrow: 1000,
                    normal: 1190,
                    large: 1350,
                    wider: 1350,
                    ie6: 1180
                };
                return(rightOrBottom === "right" ? widthMapRight : widthMapBottom)[widthType]
            }

        })

        return {
            resize: function(config) {
                if(S.one("#J_topshop")) {
                    var width = config.rightWidth
                    var height = width * MBOX.righttopRatio + (MBOX.notitle ? 0 : 55)
                    if(MBOX.qiqiaoban) {
                        height = 600
                    }
                    S.one("#J_topshop").attr("style", "width:" + width + "px;height:" + height + "px")
                }
                S.each(window.MBOX, function(mbox) {
                    if(mbox && mbox.resize) {
                        if(mbox.type === "right") {
                            mbox.resize(config.rightWidth)
                        } else {
                            mbox.resize(config.pageWidth)
                        }
                    }
                })
            }
        }
    }
})
