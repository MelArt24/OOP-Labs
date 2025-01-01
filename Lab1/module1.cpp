#include "module1.h"
#include "resource1.h"

static WCHAR* lptext;

static INT_PTR CALLBACK Work1(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);

    static int pos = 1; // ��������� ������� ��������
    static int initialPos; // ������ ��������� ������� ��������

    switch (message)
    {
    case WM_INITDIALOG:
        // ����������� ��������: ������� �� 1 �� 100
        SetScrollRange(GetDlgItem(hDlg, IDC_SCROLLBAR1), SB_CTL, 1, 100, TRUE);
        SetScrollPos(GetDlgItem(hDlg, IDC_SCROLLBAR1), SB_CTL, pos, TRUE);

        initialPos = pos;

        SetDlgItemInt(hDlg, IDC_STATIC1, pos, FALSE);
        return (INT_PTR)TRUE;

    case WM_HSCROLL:
    {
        HWND hWndScroll = GetDlgItem(hDlg, IDC_SCROLLBAR1);
        pos = GetScrollPos(hWndScroll, SB_CTL);

        switch (LOWORD(wParam))
        {
        case SB_LINELEFT: //��������� ������ ������
            pos--;
            break;
        case SB_LINERIGHT: //��������� ������ ��������
            pos++;
            break;
        case SB_THUMBPOSITION: //��������� ������� �������
        case SB_THUMBTRACK: //������� ������� �������
            pos = HIWORD(wParam);
            break;
        default: break;
        }
        SetScrollPos(hWndScroll, SB_CTL, pos, TRUE);
        SetDlgItemInt(hDlg, IDC_STATIC1, pos, FALSE); // ��������� ���������� ������
    }
    break;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK)
        {
            GetDlgItemText(hDlg, IDC_STATIC1, lptext, 4);

            EndDialog(hDlg, 1);
            return (INT_PTR)TRUE;
        }
        if (LOWORD(wParam) == IDCANCEL)
        {
            pos = initialPos;
            EndDialog(hDlg, 0);
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

int Func_MOD1(HWND hWnd, HINSTANCE hi, WCHAR* dest)
{
    lptext = dest;
    return DialogBox(hi, MAKEINTRESOURCE(IDD_DIALOG1), hWnd, Work1);
}