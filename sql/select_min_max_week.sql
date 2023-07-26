select week(min(receive_sample_date_fact)) as min, week(max(test_end_date)) as max
from viam.orders;