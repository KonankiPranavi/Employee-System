pipeline {
agent any

```
stages {
    stage('Checkout') {
        steps {
            checkout scm
            echo 'Employee System code downloaded from GitHub.'
        }
    }

    stage('Check Project Files') {
        steps {
            bat 'dir'
            echo 'Project files checked successfully.'
        }
    }
}
```

}
