#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_cell_magic('bash', '', 'sudo chmod 400 llave.pem')


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'ssh -i "llave.pem" ubuntu@ec2-18-224-140-233.us-east-2.compute.amazonaws.com "bash smsfire.sh; exit"')


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'ssh -i "llave.pem" ubuntu@ec2-18-224-140-233.us-east-2.compute.amazonaws.com "bash smsbattery.sh; exit"')


# In[ ]:




