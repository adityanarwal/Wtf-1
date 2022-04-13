**#ERROR**
**Module:** `{func.__module__}`
**Command:** `(Noting, Custom Filter)`
**Traceback:**
`{e}`
**Forward this to @Its_romeoo**
"""
                    if len(error_text) > 4000:
                        clean_error_text = await rm_markdown(error_text)
                        file = open("error_nexaub.txt", "w+")
                        file.write(clean_error_text)
                        file.close()
                        await NEXAUB.send_document(LOG_CHANNEL_ID, "error_nexaub.txt", caption="𝐄𝐫𝐫𝐨𝐫 𝟒𝟎𝟒 !! Something went wrong, Please wait for developers to Fix It.")
                        os.remove("error_nexaub.txt")
                    else:
                        await NEXAUB.send_message(chat_id=LOG_CHANNEL_ID, text=error_text)
                message.continue_propagation()
            self.add_handler(x_wrapper_cf, custom_filters, handler_group)
            return x_wrapper_cf
        return decorate_nexaub_cf
