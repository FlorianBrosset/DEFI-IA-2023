# Base image from pytorch
FROM pytorch/pytorch
# Set up for your local zone an UTC information
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
# Additional librairies
RUN pip install gradio tensorboard
RUN pip install markupsafe==2.0.1
RUN pip install pandas==1.4.3
RUN pip install numpy==1.21.6
RUN pip install sklearn==1.1.1
RUN pip install plotly==5.9.0
RUN pip install category_encoders
RUN pip install plotly
RUN pip install seaborn
RUN pip install eli5==0.13.0
RUN pip install pickle
