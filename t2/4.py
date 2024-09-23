import countries_data

data = countries_data.data


def all_languages(data_c):
    lang_list = []
    for country in range(len(data)):
        for lang in data_c[country]['languages']:
            if lang not in lang_list:
                lang_list.append(lang)
    return len(lang_list) + 1


def frequent_language(data_c):
    f_lang = {}
    for country in range(len(data)):
        for lang in data_c[country]['languages']:
            if lang in f_lang:
                f_lang[lang] = f_lang[lang] + 1
            else:
                f_lang.update({lang: 1})
    v_lang = list(f_lang.values())
    v_lang.sort(reverse=True)
    f = []
    sort = {}
    for i in v_lang:
        if len(f) < 10 and i not in f:
            f.append(i)
    for item in f:
        for country in f_lang:
            if f_lang[country] == item:
                if item not in sort:
                    sort.update({item: [country]})
                else:
                    sort[item].append(country)
    return sort


def populous(data_c):
    countries = {}
    for country in data_c:
        countries.update({country['name']: country['population']})
    p_countries = list(countries.values())
    p_countries.sort(reverse=True)
    most_populous = {}
    p_countries = p_countries[:10]
    p_countries.sort()
    for p in p_countries:
        for country in countries:
            if countries[country] == p:
                most_populous.update({country: p})
    return most_populous


print(f'all language -----> {all_languages(data)}\n')
print(f'frequent language -----> {frequent_language(data)}\n')
print(f'Most populous countries in ascending order ---- > {populous(data)}')
