import openai
import streamlit as st


def main():
    st.title('ChatGPT キャッチコピー作成アプリ')
    
    user_input = st.text_input('キャッチコピーを作成するためのキーワードを入力してください: ')
    
    if st.button('キャッチコピーを生成'):
        catchphrase = call_chatgpt_api(user_input)
        st.write('生成されたキャッチコピー: ', catchphrase)

def call_chatgpt_api(input_text):
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=input_text,
            temperature=0.7,
            max_tokens=100,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f'エラー: キャッチコピーを生成できませんでした。{str(e)}'

if __name__ == '__main__':
    main()
