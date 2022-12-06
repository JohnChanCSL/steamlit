import time
import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
import os
from pathlib import Path
import os.path
from os import path

now = datetime.now()
now = str(now)[:10]
# st.set_page_config(page_title="Doulton Hong Kong", layout="wide")
st.set_page_config(page_title="Doulton Hong Kong")
image = Image.open('')
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.title("Doulton Hong Kong - Invoice Upload System")
with col2:
    st.image(image, width=150)
with st.form('Form',clear_on_submit = True):
    name = st.text_input('Name', '')
    phone_number = st.text_input('Phone Number', '')
    amount = st.text_input('Product Amount', '')
    upload_photos = st.file_uploader('Please upload the photo(s) (Maximum 3 photos per upload)',type=['jpg', 'png', 'jpeg'], accept_multiple_files=True)
    MAX_LINES = 3
    if len(upload_photos) > MAX_LINES:
        st.error(f"Maximum number of photos reached. Only the first {MAX_LINES} will be processed.")
        upload_photos = upload_photos[:MAX_LINES]
    st.markdown('If above information is all right, please click the button below.')
    Submit = st.form_submit_button('Submit')
    if Submit:
        if len(name)*len(phone_number)*len(amount)*len(upload_photos) == 0:
            st.markdown('Please fill in all information before submit.')
        else:
            time.sleep(0.5)
            # create folder
            parent_dir = ''
            directory = str(phone_number)
            export_path = os.path.join(parent_dir, directory)
            if not path.exists(export_path):
                os.mkdir(export_path)
            else:
                i = 2
                new_export_path = os.path.join(export_path + '_' + str(i))
                while path.exists(new_export_path):
                    i += 1
                    new_export_path = export_path + '_' + str(i)
                os.mkdir(new_export_path)
                export_path = new_export_path
            if upload_photos is not None:
                for photo in upload_photos:
                    save_folder = export_path
                    save_path = Path(save_folder, photo.name)
                    with open(save_path, mode='wb') as w:
                        w.write(photo.getvalue())
            # to excel
            df_old = pd.read_excel('')
            df_old['Phone Number'] = df_old['Phone Number'].astype(str)
            df_new = pd.DataFrame(
                {'Customer Name': [str(name)], 'Phone Number': [str(phone_number)], 'Upload Date': [str(now)]})
            df = pd.concat([df_old, df_new])
            df.to_excel('C:\\Users\\cckjo\\Desktop\\DoultonHK.xlsx', index=False)
            # Message
            st.markdown('The upload process is done and details is shown as below! Thank you!')
            st.markdown('Name is ' + name)
            st.markdown('Phone number is ' + phone_number)
            st.markdown('Product amount is ' + amount)
            if upload_photos is not None:
                for photo in upload_photos:
                    image = Image.open(photo)
                    st.image(image, width=300)
            st.markdown('Please contact CS@12346578 if error is found')
