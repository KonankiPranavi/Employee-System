pipeline {
agent any

```
stages {
    stage('Checkout') {
        steps {
            checkout scm
            echo 'Employee System source code checked out successfully.'
        }
    }

    stage('Check Project Files') {
        steps {
            bat 'dir'
            echo 'Project files checked.'
        }
    }
}
```

}
