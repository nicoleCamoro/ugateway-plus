//
//  ViewController.swift
//  TouchLogin
//
//  Created by Royce Dy on 15/07/2017.
//  Copyright © 2017 rad182. All rights reserved.
//

import UIKit
import LocalAuthentication

class ViewController: UIViewController {
    
    @IBOutlet weak var activityIndicatorView: UIActivityIndicatorView!
    @IBOutlet weak var messageText: UILabel!
    @IBOutlet weak var tryAgainButton: UIButton!

    fileprivate let context = LAContext()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)
        self.promptForTouchID()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

}

extension ViewController {
    func showError(error: Error) {
        let alertViewController = UIAlertController(title: "Error", message: error.localizedDescription, preferredStyle: .alert)
        alertViewController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        self.present(alertViewController, animated: true, completion: nil)
    }
    
    func callAPI() {
        let endpoint = "http://0b8d122a.proxy.webhookapp.com/"
        guard let url = URL(string: endpoint) else {
            print("Error: cannot create URL")
            return
        }
        var urlRequest = URLRequest(url: url)
        urlRequest.httpMethod = "POST"
        // set up the session
        let config = URLSessionConfiguration.default
        let session = URLSession(configuration: config)
        
        // make the request
        let task = session.dataTask(with: urlRequest, completionHandler: { [unowned self] (data, response, error) in
            self.activityIndicatorView.stopAnimating()
            // do stuff with response, data & error here
            if let error = error {
                self.messageText.text = error.localizedDescription
                self.tryAgainButton.isHidden = false
            } else if let response = response, let data = data {
                // success!
                print(response)
                print(data)
            }
        })
        task.resume()
    }
    
    func promptForTouchID() {
        self.tryAgainButton.isHidden = true
        self.activityIndicatorView.startAnimating()
        self.messageText.text = nil
        
        context.evaluatePolicy(.deviceOwnerAuthentication, localizedReason: "Used for Login") { [unowned self] (success, error) in
            DispatchQueue.main.async(execute: {
                guard success else {
                    guard let error = error else {
                        return
                    }
                    
                    switch(error) {
                    case LAError.authenticationFailed:
                        self.messageText.text = "There was a problem verifying your identity."
                    case LAError.userCancel:
                        self.messageText.text = "Authentication was canceled by user."
                        // Fallback button was pressed and an extra login step should be implemented for iOS 8 users.
                    // By the other hand, iOS 9+ users will use the pasccode verification implemented by the own system.
                    case LAError.userFallback:
                        self.messageText.text = "The user tapped the fallback button (Fuu!)"
                    case LAError.systemCancel:
                        self.messageText.text = "Authentication was canceled by system."
                    case LAError.passcodeNotSet:
                        self.messageText.text = "Passcode is not set on the device."
                    case LAError.touchIDNotAvailable:
                        self.messageText.text = "Touch ID is not available on the device."
                    case LAError.touchIDNotEnrolled:
                        self.messageText.text = "Touch ID has no enrolled fingers."
                    // iOS 9+ functions
                    case LAError.touchIDLockout:
                        self.messageText.text = "There were too many failed Touch ID attempts and Touch ID is now locked."
                    case LAError.appCancel:
                        self.messageText.text = "Authentication was canceled by application."
                    case LAError.invalidContext:
                        self.messageText.text = "LAContext passed to this call has been previously invalidated."
                    // MARK: IMPORTANT: There are more error states, take a look into the LAError struct
                    default:
                        self.messageText.text = "Touch ID may not be configured"
                        break
                    }
                    self.activityIndicatorView.stopAnimating()
                    // show try again button
                    self.tryAgainButton.isHidden = false
                    
                    return
                }
                // success
                self.callAPI()
            })
        }
    }
}

