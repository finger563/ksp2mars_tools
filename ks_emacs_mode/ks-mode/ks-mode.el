;; Kerboscirpt emacs mode file

;; Hook for users to run their own code on loading this mode
(defvar ks-mode-hook nil)

;;;###autoload
(add-to-list 'auto-mode-alist '("\\.ks\\'" . ks-mode))

;; command to comment/uncomment text
(defun ks-comment-dwim (arg)
  "Comment or uncomment current line or region in a smart way. For detail, see `comment-dwim'."
  (interactive "*P")
  (require 'newcomment)
  (let (
        (comment-start "//") (comment-end "")
        )
    (comment-dwim arg)))

(defun ks-indent-line ()
  "Indent current line as kerboscript code"
  (interactive)
  (beginning-of-line)
  (if (bobp)
      (indent-line-to 0)
    (let ((not-indented t) cur-indent)
      (if (looking-at "^[ \t]*\\(}\.\\|}[ \t]*$\\)")
          (progn
            (save-excursion
              (forward-line -1)
              (setq cur-indent (- (current-indentation) default-tab-width)))
            (if (< cur-indent 0)
                (setq cur-indent 0)))
        (save-excursion
          (while not-indented
            (forward-line -1)
            (if (looking-at "^[ \t]*\\(}\.\\|}[ \t]*$\\)")
                (progn
                  (setq cur-indent (current-indentation))
                  (setq not-indented nil))
              (if (looking-at "^[ \t]*\\(if.*{\\|.*else.*{\\|until.*{\\|for.*{\\|when.*then.*{\\|on.*{\\|function.*{\\)")
                  (progn
                    (setq cur-indent (+ (current-indentation) default-tab-width))
                    (setq not-indented nil))
                (if (bobp)
                    (setq not-indented nil)))))))
      (if cur-indent
          (indent-line-to cur-indent)
        (indent-line-to 0)))))

(defvar ks-mode-map
  (let ((map (make-sparse-keymap)))
    (define-key map (kbd "RET") 'newline-and-indent)
    (define-key map "\C-j" 'newline-and-indent)
    map)
  "Keymap for kerboscript major mode")

(setq kos-kwdList
      '("to" "set" "if" "until" "lock" "unlock" "print" "on" "toggle" "wait" "when" "identifier" "stage" "clearscreen" "add" "remove" "log" "break" "preserve" "declare" "switch" "copy" "rename" "delete" "edit" "run" "list" "reboot" "shutdown" "for" "unset" "batch" "deploy" "local" "global" "is" "function" "else")
      )

(setq kerboscript-keywords
      `(
        ( ,(regexp-opt kos-kwdList 'words) . font-lock-keyword-face)
        ( ,(regexp-opt '("Pi") 'words)     . font-lock-constant-face)
        )
      )

;; syntax table
(defvar ks-syntax-table nil "Syntax table for `ks-mode'.")
(setq ks-syntax-table
      (let ((synTable (make-syntax-table)))
        
        ;; C style comment: “// …”
        (modify-syntax-entry ?\/ ". 12b" synTable)
        (modify-syntax-entry ?\n "> b" synTable)
        
        synTable))

(define-derived-mode ks-mode prog-mode "KerboScript script"
  "Major mode for editing KerboScript files"
  :syntax-table ks-syntax-table
  
  (setq font-lock-defaults '(kerboscript-keywords))
  (set (make-local-variable 'indent-line-function) 'ks-indent-line)
  (setq mode-name "ks")

  ;; modify the keymap
  (define-key ks-mode-map [remap comment-dwim] 'ks-comment-dwim)
  )

(provide 'ks-mode)
