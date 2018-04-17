from app.email import verify_email

def test_basic_email_text_only():
  assert verify_email("name@email.com") == True

def test_basic_email_with_numbers():
  assert verify_email("n1a2m3e4@email.com") == True

def test_email_with_periods():
  assert verify_email("n.a.m.e@email.com") == True

def test_email_with_begining_period():
  assert verify_email(".n.a.m.e@email.com") == False

def test_email_with_ending_period():
  assert verify_email("n.a.m.e.@email.com") == False

def test_email_with_two_periods():
  assert verify_email("na..me@email.com") == False

def test_email_starting_with_number():
  assert verify_email("1name@email.com") == False

def test_email_with_symbols():
  assert verify_email("!$%*+-=?^_{|}~@email.com") == True

def test_email_with_sub_domain():
  assert verify_email("test@email.org.us") == True

def test_email_with_no_at_or_domain():
  assert verify_email("not_email") == False

def test_email_with_no_domain():
  assert verify_email("not_email@") == False

def test_email_with_no_at():
  assert verify_email("not_emaildomain.com") == False

def test_email_with_hyphen_in_domain():
  assert verify_email("test@email-1.org") == True

def test_email_with_hyphen_beginining_domain():
  assert verify_email("test@-aa.net") == False

def test_email_with_hyphen_ending_domain():
  assert verify_email("test@aa-.net") == False

def test_email_with_numbers_for_domain():
  assert verify_email("test@369.com.au") == True

def test_email_with_1_letter_domain():
  assert verify_email("test@a.net") == True

def test_email_with_1_number_domain():
  assert verify_email("test@1.net") == True

def test_email_with_too_long_domain():
  assert verify_email("test@1234567890123456789012345678901234567890123456789012345678901234567890.net") == False

def test_email_with_punycode_domain():
  assert verify_email("test@xn--74h.com") == True

def test_email_with_domain_and_subdomains():
  assert verify_email("test@a.asdf.asdfjkl.df.net.aa") == True
