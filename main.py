

# sudo code

def params:
  #defaults
  notif_freq = 1 #days
  notif_ct = 3 # files
  
  user_dialog
  set_params

def folder_watch:
  set_dir
  watch_dir
  collect_files
  return


def notification:
  notif_timer = core.wait()
  
  def notif_dialog:
    display_file
    display_actions
    get_user_input
      cleanup_files.update()
    # refresh_file()
    cleanup_files
    return
  
  return

def cleanup:
  for file,action in cleanup_files:
    action(file) # action = move, del, rename
  return
  
def runny_runtime:
  do_it_all
  
  return

runny_runtime()
