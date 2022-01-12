# This function return the String in Camel Case Format.


def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]


a = "+the;best-way/to+write.the=camel?case*format"
print(camelCase(a))