Name: clean payments 1615 customer
model: payment

Code :
# Available variables:
#  - env: Odoo Environment on which the action is triggered
#  - model: Odoo Model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: Odoo function to compare floats based on specific precisions
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - UserError: Warning Exception to use with raise
#  - Command: x2Many commands namespace
# To return an action, assign: action = {...}

# raise UserError('qlq')


for rec in records:
  journal_entry = env['account.move'].search([('payment_id','=',rec.id)])
  account_receivable_line = journal_entry.line_ids.filtered(lambda x: x.account_id.id == 6)  # account receivable id 
  
  # raise UserError(account_receivable_line.id)
  # raise UserError(f"{journal_entry.line_ids.ids} | {journal_entry.line_ids.mapped('matching_number')}")
  
  lines_to_link = env['account.move.line'].search([('matching_number','=',account_receivable_line.matching_number)])
  
  journal_entry.button_draft()
  line_to_change = journal_entry.line_ids.filtered(lambda x: x.account_id.id == 526)  # bank account 
  
  line_to_change['account_id'] = 36 # Bank Suspense Account
  
  journal_entry.action_post()
  
  # raise UserError(lines_to_link.mapped('move_id'))
  lines_to_link.reconcile()
  
  rec['x_studio_fixed'] = True
  

  # raise UserError(journal_entry)
