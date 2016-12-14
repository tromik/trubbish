#requires -module PowerLine
using module PowerLine

$PowerLinePrompt = @(
        @{ bg = "Cyan";     fg = "White"; text = { $MyInvocation.HistoryId } }
        @{ bg = "DarkBlue"; fg = "White"; text = { $pwd } }
    )

Set-PowerLinePrompt -PowerLineFont
