def is_khnu_page(text):
    #return True if page exist
    start_str = '<div style="margin: 0px 20px 40px 40px; min-height: 500px;">'
    index = text.find(start_str) + len(start_str)
    result = text[index: index + 6]
    if result == '</div>':
        return False
    else:
        return True