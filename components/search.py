from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton, \
    ForceReply
from telegram.ext import ConversationHandler

import captions
import const
import search
import settings
import util
from components import basic
from components.explore import send_bot_details
from dialog import messages


def search_query(bot, update, chat_data, query, send_errors=True):
    cid = update.effective_chat.id

    results = search.search_bots(query)

    is_admin = cid in settings.MODERATORS
    reply_markup = ReplyKeyboardMarkup(
        basic.main_menu_buttons(is_admin),
        resize_keyboard=True
    ) if util.is_private_message(update) else ReplyKeyboardRemove()
    if results:
        if len(results) == 1:
            return send_bot_details(bot, update, chat_data, results[0])
        too_many_results = len(results) > settings.MAX_SEARCH_RESULTS

        results = ''
        if cid in settings.MODERATORS:
            # append edit buttons
            results += '\n'.join(["{} — /edit{} 🛃".format(b, b.id) for b in list(results)[:100]])
        else:
            results += '\n'.join([str(b) for b in list(results)[:settings.MAX_SEARCH_RESULTS]])
        results += '\n…' if too_many_results else ''
        results = messages.SEARCH_RESULTS.format(bots=results, num_results=len(results),
                                                   plural='s' if len(results) > 1 else '',
                                                   query=query)
        update.message.reply_text(results, parse_mode=ParseMode.MARKDOWN, reply_markup=reply_markup)
    else:
        if send_errors:
            update.message.reply_text(
                util.failure("Sorry, I couldn't find anything related "
                             "to *{}* in the @BotList. /search".format(util.escape_markdown(query))),
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=reply_markup)
    return ConversationHandler.END


def search_handler(bot, update, chat_data, args=None):
    if args:
        search_query(bot, update, chat_data, ' '.join(args))
    else:
        # no search term
        if util.is_group_message(update):
            action = const.DeepLinkingActions.SEARCH
            update.message.reply_text(
                "Please use the search command with arguments, inlinequeries or continue in private. "
                "Example: `/search awesome bot`",
                quote=True,
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton('🔎 Search inline', switch_inline_query_current_chat=''),
                        InlineKeyboardButton(captions.SWITCH_PRIVATE,
                                             url="https://t.me/{}?start={}".format(
                                                 settings.SELF_BOT_NAME,
                                                 action
                                             ))
                    ]]
                ))
        else:
            update.message.reply_text(messages.SEARCH_MESSAGE, reply_markup=ForceReply(selective=True))
    return ConversationHandler.END
