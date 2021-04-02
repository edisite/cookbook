odoo.define('gtica_whatsapp_live.whatsapp_live', function (require) {
'use strict';

require('web.dom_ready');

(function ($, window) {
  'use strict';

  window.gtica_apiwhatsapp = window.gtica_apiwhatsapp || {};

  gtica_apiwhatsapp = $.extend({
    $apiwhatsapp: null,
    chatbox: false,
    is_mobile: false,
  }, gtica_apiwhatsapp);


  gtica_apiwhatsapp.chatbox_show = function () {
    gtica_apiwhatsapp.$apiwhatsapp.addClass('whatsappapi--chatbox');
    gtica_apiwhatsapp.chatbox = true;
       // Trigger custom event
    $(document).trigger('whatsappapi:show');
  };

  gtica_apiwhatsapp.chatbox_hide = function () {
    gtica_apiwhatsapp.$apiwhatsapp.removeClass('whatsappapi--chatbox whatsappapi--tooltip');
    gtica_apiwhatsapp.chatbox = false;
    // Trigger custom event
    $(document).trigger('whatsappapi:hide');
  };

$(function(){gtica_apiwhatsapp.$apiwhatsapp=$('.whatsappapi');gtica_apiwhatsapp.is_mobile=!!navigator.userAgent.match(/Android|iPhone|BlackBerry|IEMobile|Opera Mini/i);if(gtica_apiwhatsapp.$apiwhatsapp.length){whatsappapi_magic()}
function whatsappapi_magic(){var button_delay=2*1000;var chat_delay=1*1000;var has_cta='';var timeoutHover,timeoutCTA;function chatbox_show(){clearTimeout(timeoutCTA);gtica_apiwhatsapp.chatbox_show()}
function chatbox_hide(){gtica_apiwhatsapp.chatbox_hide()}
function apiwhatsapp_click(){if(!gtica_apiwhatsapp.chatbox){chatbox_show()}else{if(gtica_apiwhatsapp.chatbox){chatbox_hide()}
$(document).trigger('whatsappapi:open')}}
if(gtica_apiwhatsapp.is_mobile){var classes='whatsappapi--show';if(!chat_delay){classes+=' whatsappapi--tooltip'}
setTimeout(function(){gtica_apiwhatsapp.$apiwhatsapp.addClass(classes)},button_delay)}
if(!gtica_apiwhatsapp.is_mobile){$('.whatsappapi__button',gtica_apiwhatsapp.$apiwhatsapp).mouseenter(function(){if(!gtica_apiwhatsapp.chatbox)timeoutHover=setTimeout(chatbox_show,1500)}).mouseleave(function(){clearTimeout(timeoutHover)})}
$('.whatsappapi__button',gtica_apiwhatsapp.$apiwhatsapp).click(apiwhatsapp_click);$('.whatsappapi__close',gtica_apiwhatsapp.$apiwhatsapp).click(chatbox_hide);$('.whatsappapi__box__scroll').on('mousewheel DOMMouseScroll',function(e){e.preventDefault();var delta=e.originalEvent.wheelDelta||-e.originalEvent.detail;this.scrollTop+=(delta<0?1:-1)*30});if(gtica_apiwhatsapp.is_mobile){var initial_height=window.innerHeight;var timeoutKB;$(document).on('focus blur','input, textarea',function(){clearTimeout(timeoutKB);timeoutKB=setTimeout(function(){gtica_apiwhatsapp.$apiwhatsapp.toggleClass('whatsappapi--show',initial_height*0.7<window.innerHeight)},800)})}
$(document).on('click','.apiwhatsapp_open',function(e){e.preventDefault();if(!gtica_apiwhatsapp.chatbox)apiwhatsapp_click()});$(document).trigger('whatsappapi:start')}})

}(jQuery, window));
});

