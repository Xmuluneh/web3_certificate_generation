from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from connection.models import ApiModels.Account
import json

@require_POST
def check_account(request):
    try:
        data = json.loads(request.body)
        address = data.get('address')

        if not address:
            return JsonResponse({'success': False, 'message': 'Address is required'})

        address = str(address).strip()
        fetched_account = Account.objects.filter(address=address).first()

        if fetched_account:
            return JsonResponse({
                'success': True,
                'account': {
                    'address': fetched_account.address,
                    'first_name': fetched_account.first_name,
                    'last_name': fetched_account.last_name,
                    'is_admin': fetched_account.is_admin,
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'No account found', 'status_code': 111})

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@require_POST
def create_account(request):
    try:
        data = json.loads(request.body)
        address = data.get('address')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        is_admin = data.get('is_admin', False)

        if not (address and first_name and last_name):
            return JsonResponse({'success': False, 'message': 'All fields are required'})

        address = str(address).strip()
        fetched_address = Account.objects.filter(address=address)

        if not fetched_address:
            first_name = str(first_name).strip()
            last_name = str(last_name).strip()

            account = Account.objects.create(address=address, first_name=first_name, last_name=last_name, is_admin=is_admin)

            return JsonResponse({
                'success': True,
                'message': 'Account created',
                'account': {
                    'address': account.address,
                    'first_name': account.first_name,
                    'last_name': account.last_name,
                    'is_admin': account.is_admin,
                }
            })
        else:
            return JsonResponse({'success': False, 'message': 'Address already registered'})

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})

@require_POST
def file_upload_and_save_asset(request):
    try:
        if request.method == 'POST':
            myfile = request.FILES.get('file')
            address = request.POST.get('address')
            asset_id = request.POST.get('asset_id')

            if not (myfile and address and asset_id):
                return JsonResponse({'success': False, 'message': 'All fields are required'})

            address = str(address).strip()
            account = Account.objects.filter(address=address).first()

            if not account:
                return JsonResponse({'success': False, 'message': 'Account not found'})

            fs = FileSystemStorage()
            file_name = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(file_name)

            asset_obj = Assets.objects.create(account=account, asset_index=asset_id, image_url=uploaded_file_url)

            if asset_obj:
                return JsonResponse({
                    'success': True,
                    'asset': {
                        'id': asset_obj.id,
                        'asset_index': asset_obj.asset_index,
                        'account': asset_obj.account.address,
                        'image_url': asset_obj.image_url,
                    },
                    'message': 'Uploaded'
                })
            else:
                return JsonResponse({'success': False, 'message': 'File upload failed'})

        else:
            return JsonResponse({'success': False, 'message': f'Method {request.method} not allowed'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
@require_POST
def set_asset_index(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            asset_id = data.get('asset_id')
            asset_index = data.get('asset_index')
            ipfs_url = data.get('ipfs_url')
            asset_name = data.get('asset_name')

            if not (asset_id and asset_index and ipfs_url):
                return JsonResponse({'success': False, 'message': 'All fields are required'})

            asset = Assets.objects.filter(id=int(asset_id)).first()

            if asset:
                asset.asset_index = asset_index
                asset.account.request_status = True
                asset.account.save()
                asset.ipfs_url = ipfs_url
                asset.asset_name = asset_name
                asset.save()

                return JsonResponse({'success': True, 'message': 'Updated'})
            else:
                return JsonResponse({'success': False, 'message': 'Asset not found'})
        else:
            return JsonResponse({'success': False, 'message': f'Method {request.method} not allowed'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
@require_POST
def get_all_requests(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')

            if not address:
                return JsonResponse({'success': False, 'message': 'Address is required'})

            address = str(address).strip()
            fetched_account = Account.objects.filter(address=address).first()

            if not (fetched_account and fetched_account.is_admin):
                return JsonResponse({'success': False, 'message': 'Access Denied'})

            accounts_list = Account.objects.filter(has_requested=True, request_status=False, is_admin=False)
            ls = []

            for acc in accounts_list:
                ls.append({
                    'id': acc.id,
                    'address': acc.address,
                    'first_name': acc.first_name,
                    'last_name': acc.last_name,
                    'is_admin': acc.is_admin,
                    'request_status': acc.request_status,
                    'has_requested': acc.has_requested,
                })

            return JsonResponse({'success': True, 'account_list': ls})

        else:
            return JsonResponse({'success': False, 'message': f'Method {request.method} not allowed'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
@require_POST
def get_assets_trainee(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')

            if not address:
                return JsonResponse({'success': False, 'message': 'Address is required'})

            address = str(address).strip()
            fetched_account = Account.objects.filter(address=address).first()

            if not fetched_account:
                return JsonResponse({'success': False, 'message': 'Account not found'})

            assets = Assets.objects.filter(account=fetched_account).order_by('-id')
            ls = []

            for asset in assets:
                ls.append({
                    'id': asset.id,
                    'asset_index': asset.asset_index,
                    'asset_name': asset.asset_name,
                    'asset_status': asset.asset_status,
                    'image_url': f"https://algorand-endpoint.herokuapp.com{asset.image_url}",
                    # 'image_url': f"http://127.0.0.1:8000{asset.image_url}",
                    'account': {
                        'id': asset.account.id,
                        'address': asset.account.address,
                        'first_name': asset.account.first_name,
                        'last_name': asset.account.last_name,
                        'is_admin': asset.account.is_admin,
                        'request_status': asset.account.request_status,
                        'has_requested': asset.account.has_requested,
                    }
                })

            return JsonResponse({'success': True, 'asset_list': ls})

        else:
            return JsonResponse({'success': False, 'message': f'Method {request.method} not allowed'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
@require_POST
def set_asset_final_status(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            asset_id = data.get('asset_id')

            if not asset_id:
                return JsonResponse({'success': False, 'message': 'Asset ID is required'})

            asset = Assets.objects.filter(id=int(asset_id)).first()

            if not asset:
                return JsonResponse({'success': False, 'message': 'Asset not found'})

            asset.asset_status = True
            asset.save()

            return JsonResponse({'success': True, 'message': 'Updated'})

        else:
            return JsonResponse({'success': False, 'message': f'Method {request.method} not allowed'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})


@require_POST
def create_trainee_request(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            address = data.get('address')

            if not address:
                return JsonResponse({'success': False, 'message': 'Address is required'})

            address = str(address).strip()
            fetched_account = Account.objects.filter(address=address).first()

            if not fetched_account:
                return JsonResponse({'success': False, 'message': 'Account not found'})

            fetched_account.has_requested = True
            fetched_account.request_status = False
            fetched_account.save()

            return JsonResponse({'success': True, 'message': 'Requested successfully'})

        else:
            return JsonResponse({'success': False, 'message': f'Method {request.method} not allowed'})

    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})
    