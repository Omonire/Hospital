from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_sample_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Department = apps.get_model('departments', 'Department')
    Patient = apps.get_model('patients', 'Patient')
    Referral = apps.get_model('referrals', 'Referral')

    # Create admin user (or get if already exists)
    admin_user, _ = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@hospital.com',
            'password': make_password('password'),
            'role': 'admin',
            'is_staff': True,
            'is_superuser': True
        }
    )

    # Create Departments
    pharmacy_dept = Department.objects.create(name='Pharmacy', created_by=admin_user)
    lab_dept = Department.objects.create(name='Lab', created_by=admin_user)
    cashier_dept = Department.objects.create(name='Cashier', created_by=admin_user)
    records_dept = Department.objects.create(name='Records', created_by=admin_user)

    # Create Users
    doctor_user = User.objects.create_user(username='doctor_a', password='password', role='doctor', first_name='Alice', last_name='Anderson')
    nurse_user = User.objects.create_user(username='nurse_b', password='password', role='nurse', first_name='Bob', last_name='Brown')

    User.objects.create_user(username='records_c', password='password', role='records', department=records_dept, first_name='Charlie', last_name='Clark')
    User.objects.create_user(username='pharmacy_d', password='password', role='pharmacy', department=pharmacy_dept, first_name='David', last_name='Davis')
    User.objects.create_user(username='lab_e', password='password', role='lab', department=lab_dept, first_name='Eve', last_name='Evans')
    User.objects.create_user(username='cashier_f', password='password', role='cashier', department=cashier_dept, first_name='Frank', last_name='Franklin')

    # Create Patients
    patient1 = Patient.objects.create(name='John Smith', age=45, gender='male', contact_info='555-0101', medical_history='Hypertension', created_by=admin_user)
    patient2 = Patient.objects.create(name='Jane Doe', age=32, gender='female', contact_info='555-0102', medical_history='Asthma', created_by=admin_user)

    # Create Referrals
    Referral.objects.create(patient=patient1, from_doctor=doctor_user, to_department=pharmacy_dept, status='pending')
    Referral.objects.create(patient=patient2, from_doctor=doctor_user, to_department=lab_dept, status='in_progress')


def delete_sample_data(apps, schema_editor):
    User = apps.get_model('users', 'User')
    Department = apps.get_model('departments', 'Department')
    Patient = apps.get_model('patients', 'Patient')
    Referral = apps.get_model('referrals', 'Referral')

    # Be careful with deleting users, especially the admin user.
    # We will delete only the sample users we created.
    User.objects.filter(username__in=['doctor_a', 'nurse_b', 'records_c', 'pharmacy_d', 'lab_e', 'cashier_f']).delete()
    Department.objects.filter(name__in=['Pharmacy', 'Lab', 'Cashier', 'Records']).delete()
    Patient.objects.filter(name__in=['John Smith', 'Jane Doe']).delete()
    # Referrals will be deleted automatically due to CASCADE on patient foreign key.

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('departments', '0001_initial'),
        ('patients', '0001_initial'),
        ('referrals', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_data, delete_sample_data),
    ]
